# FastAPI学習

[FastAPI](https://fastapi.tiangolo.com/)
[FastAPI入門](https://zenn.dev/sh0nk/books/537bb028709ab9)

## 実行

```sh
docker compose up
```

Swagger UI
http://localhost:8000/docs

## DB初期化

```sh
docker compose exec app poetry run python -m api.migrate_db
```

## テスト

```sh
docker compose run --rm --entrypoint "poetry run pytest --asyncio-mode=auto" app
```
