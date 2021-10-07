import pandas as pd
import numpy as np
import json

from .path import get_path_from_root
from .memoize import memoize
from .response import json_from_df

source = {
    "src_url": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
    "src_label": "Schul- und Sportdepartement, Stadt Zürich",
}


def _load_data():
    df = pd.read_csv(
        get_path_from_root("data/random_facts/data.csv"),
        parse_dates=[],
        dtype={},
    )
    df = df.rename(
        columns={
            "RaumNr": "placeId",
            "Raum": "placeName",
            "Oberthema": "category",
            "Zahl": "value",
            "Thema": "topic",
        }
    )
    df = df.drop(columns=["Vergleichszahl", "Vergleichstext", "Bemerkungen"])
    df["topic_slug"] = df["topic"].str.extract(r"^([^:]+)", expand=True)[0]
    return df


load_data = memoize(_load_data)


def make_answer_fact(topic_slug, unit):
    def answer_fact():
        df = load_data()
        df = df[df["topic_slug"] == topic_slug]
        if df.empty:
            raise ValueError("unknown topic")
        df = df[df["placeId"] <= 12]
        df = df[["placeId", "placeName", "value"]]
        return {
            "unit": unit,
            "values": json.loads(json_from_df(df)),
        }

    return answer_fact
