import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances
from tqdm import tqdm
import re
import json

from .questions import questions
from .search import load_embeddings_dict, rough_tokenize

good_word_threshold = 25


def chunk_name_from_word(w):
    l = 2
    return w[:l].ljust(l, "_")


def assert_sorted(l):
    for i in range(1, len(l)):
        assert l[i - 1] <= l[i]


def prepare_static_search(out_folder):
    embeddings_dict = load_embeddings_dict()

    # BEGIN load query and question words

    query_words = []
    for w in embeddings_dict.keys():
        if rough_tokenize(w, embeddings_dict) == [w]:
            query_words.append(w)
    query_words.sort()
    print("len(query_words)", len(query_words))

    query_word_embeddings = np.array([embeddings_dict[w] for w in query_words])

    question_words = []
    question_words_ids = []
    for q in questions:
        for w in rough_tokenize(q["text"], embeddings_dict):
            if w not in embeddings_dict:
                continue
            question_words.append(w)
            question_words_ids.append(q["id"])
    print("len(question_words)", len(question_words))

    question_word_embeddings = np.array([embeddings_dict[w] for w in question_words])

    # BEGIN calculate pairwise distances between words

    query_question_distances = pairwise_distances(
        query_word_embeddings, question_word_embeddings
    )
    print(
        "query_question_distances.shape before filtering for good words",
        query_question_distances.shape,
    )
    good_word_mask = query_question_distances.min(axis=1) <= np.sqrt(
        good_word_threshold
    )
    query_words = list(np.array(query_words)[good_word_mask])
    query_word_embeddings = query_word_embeddings[good_word_mask]
    query_question_distances = query_question_distances[good_word_mask]
    print(
        "query_question_distances.shape after filtering for good words",
        query_question_distances.shape,
    )

    # BEGIN make sure that questions have consecutive ids

    question_ids = [q["id"] for q in questions]
    question_ids.sort()
    assert question_ids[0] == 1
    assert question_ids[-1] == len(question_ids)

    # BEGIN group pairwise distances by question

    temp = [None for q in questions]
    for q in questions:
        word_indices = []
        for word_index, question_id in enumerate(question_words_ids):
            if question_id == q["id"]:
                word_indices.append(word_index)
        temp[q["id"] - 1] = np.min(query_question_distances[:, word_indices], axis=1)
    query_question_distances = np.array(temp).T
    print(
        "query_question_distances.shape after grouping by question",
        query_question_distances.shape,
    )
    del temp

    # BEGIN group words into chunks

    word_indices_by_chunk = {}
    for i, w in enumerate(query_words):
        chunk_name = chunk_name_from_word(w)
        if chunk_name not in word_indices_by_chunk:
            word_indices_by_chunk[chunk_name] = []
        word_indices_by_chunk[chunk_name].append(i)
    print("len(word_indices_by_chunk)", len(word_indices_by_chunk))

    # BEGIN save chunks

    for chunk_name, word_indices in word_indices_by_chunk.items():
        chunk_words = [query_words[i] for i in word_indices]
        assert_sorted(chunk_words)

        with (out_folder / f"chunk_{chunk_name}_words.json").open(
            "w", encoding="utf-8"
        ) as f:
            json.dump(chunk_words, f)

        with (out_folder / f"chunk_{chunk_name}_distances").open("wb") as f:
            query_question_distances[word_indices, :].astype(np.float32).tofile(f)
