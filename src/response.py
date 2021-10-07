from fastapi import Response


def json_from_df(df):
    return df.to_json(orient="records", date_format="iso")


def response_from_df(df):
    return Response(
        content=json_from_df(df),
        media_type="application/json",
    )
