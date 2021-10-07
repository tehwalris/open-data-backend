This is the backend of [ask-open-data.ch](https://ask-open-data.ch). See [N3XT191/open-data-frontend](https://github.com/N3XT191/open-data-frontend) for information about the project (including [developer documentation for this backend](https://github.com/N3XT191/open-data-frontend/blob/main/doc/developing.md#backend)).

```shell
./download-data.sh
python -m src.preprocess
uvicorn main:app --reload
```
