This is the backend of [ask-open-data.ch](https://ask-open-data.ch). See [N3XT191/open-data-frontend](https://github.com/N3XT191/open-data-frontend) for information about the project.

```shell
./download-data.sh
python -m src.preprocess
uvicorn main:app --reload
```
