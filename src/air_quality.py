import pandas as pd
import numpy as np
import glob
from tqdm import tqdm

from .response import response_from_df
from .memoize import memoize
from .path import get_path_from_root
from .smooth import smooth

source = {
    "src_url": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
    "src_label": "Gesundheits- und Umweltdepartement, Stadt Zürich",
}


def get_all_air_quality_csv_paths():
    # TODO
    return glob.glob(str(get_path_from_root("data/air_quality/*.csv")))


def load_single_air_quality_csv(path):
    df = pd.read_csv(
        path,
        parse_dates=["Datum"],
        dtype={
            "Standort": "category",
            "Parameter": "category",
        },
    )
    df = df[(df["Status"] == "bereinigt") | (df["Status"] == "provisorisch")]
    df = df.drop(columns=["Intervall", "Status"])
    df = df.rename(
        columns={
            "Datum": "date",
            "Standort": "location",
            "Parameter": "pollutant",
            "Einheit": "unit",
            "Wert": "value",
        }
    )
    df = df.set_index("date")
    return df


def _load_air_quality(group_by):
    day_df = [
        load_single_air_quality_csv(path)
        for path in tqdm(get_all_air_quality_csv_paths())
    ]
    day_df = pd.concat(day_df)
    day_df = day_df.groupby([group_by(day_df.index), "location", "pollutant"]).mean()
    return day_df


def get_monthly_air_quality():
    df = pd.read_pickle(get_path_from_root("data/air_quality/pre/monthly.pickle"))
    df.index.rename("date", level=0, inplace=True)
    return df


def get_day_of_year_air_quality():
    df = pd.read_pickle(get_path_from_root("data/air_quality/pre/day_of_year.pickle"))
    df.index.rename("day_of_year", level=0, inplace=True)
    return df


def get_hour_air_quality():
    df = pd.read_pickle(get_path_from_root("data/air_quality/pre/hour.pickle"))
    df.index.rename("hour", level=0, inplace=True)
    return df


def make_answer_pollutant_over_time(pollutant):
    def answer_pollutant_over_time():
        df = get_monthly_air_quality()
        df = df.loc[pd.IndexSlice[:, :, pollutant]]
        df = df.groupby(pd.Grouper(freq="M", level="date")).mean().reset_index()
        df = df.rename(columns={"date": "x", "value": "y"})
        df = smooth(df, "y", window_size=12)
        return response_from_df(df)

    return answer_pollutant_over_time


def answer_combined_over_time():
    df = get_monthly_air_quality()
    df = df.reset_index()
    df = df.groupby(["date", "pollutant"]).mean()["value"].unstack("pollutant")
    df = df.sort_index()
    df = df / df.iloc[0]
    df = df.mean(axis=1)
    df = df.reset_index()
    df = df.rename(columns={"date": "x", 0: "y"})
    df = smooth(df, "y", window_size=12)
    return response_from_df(df)


def answer_over_year():
    df = get_day_of_year_air_quality()
    df = df.reset_index()
    df = df.groupby(["day_of_year", "pollutant"]).mean()["value"].unstack("pollutant")
    df.columns = df.columns.astype("string")
    df = df[["PM10", "CO", "O3"]]
    df = df.sort_index()
    df = df / df.max(axis=0)
    df = df.reset_index()
    return response_from_df(df)


def answer_over_day():
    df = get_hour_air_quality()
    df = df.reset_index()
    df = df.groupby(["hour", "pollutant"]).mean()["value"].unstack("pollutant")
    df.columns = df.columns.astype("string")
    df = df[["PM10", "CO", "O3"]]
    df = df.sort_index()
    df = df / df.max(axis=0)
    df = df.reset_index()
    return response_from_df(df)


def answer_pollutant_table():
    df = get_monthly_air_quality()
    df = df.reset_index()
    date = df["date"].max()
    df = df[df["date"] == date]
    df = df.groupby("pollutant").mean()
    return {
        "date": date,
        "values": df.to_dict()["value"],
    }
