import pandas as pd
import numpy as np
import json

from .path import get_path_from_root
from .memoize import memoize
from .response import json_from_df, response_from_df

source = {
    "src_url": "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand",
    "src_label": "Stadtpolizei Zürich",
}


def _load_data():
    df = pd.read_csv(
        get_path_from_root("data/dogs/data.csv"),
        dtype={
            "status": "category",
        },
    )
    return df


load_data = memoize(_load_data)


def dog_gender():
    df = load_data()
    df = df["GESCHLECHT_HUND"].value_counts()

    df = df.reset_index()
    df.columns = ["x", "y"]
    return response_from_df(df)


def owner_gender():
    df = load_data()
    df = df["GESCHLECHT"].value_counts()

    df = df.reset_index()
    df.columns = ["x", "y"]
    return response_from_df(df)


def dog_breed():
    df = load_data()
    temp = df["RASSE1"].value_counts().sort_values().to_frame()
    size = temp.size
    others = df["RASSE1"].value_counts().tail(size - 10).sum()
    temp = df["RASSE1"].value_counts().head(10)

    temp["Andere"] = others
    temp = temp.to_frame()
    temp = temp.reset_index()
    temp.columns = ["x", "y"]

    temp = temp.iloc[::-1]

    return response_from_df(temp)


def dogs_by_kreis():
    df = load_data()
    df = df["STADTKREIS"].value_counts().sort_index()
    df[0] = df.sum()
    df = df.to_frame()
    df = df.reset_index()
    df.columns = ["placeId", "value"]

    return {
        "unit": "dogs",
        "values": json.loads(json_from_df(df)),
    }


def owner_age():
    df = load_data()
    df = df["ALTER"].value_counts().sort_index().to_frame()

    df = df.reset_index()
    df.columns = ["x", "y"]
    return response_from_df(df)


def dog_age():
    df = load_data()
    df = df["GEBURTSJAHR_HUND"].value_counts()
    df = df[df > 1].sort_index()

    df = df.reset_index()
    df.columns = ["x", "y"]
    return response_from_df(df)


def max_dog_count():
    df = load_data()
    df = df["HALTER_ID"].value_counts().head(1).to_frame()

    df = df.reset_index()
    df.columns = ["x", "y"]
    return response_from_df(df)
