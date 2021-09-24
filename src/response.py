from fastapi import Response

def response_from_df(df):
  return Response(
    content=df.to_json(orient='records', date_format='iso'),
    media_type="application/json",
  )