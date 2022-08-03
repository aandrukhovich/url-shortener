# url-shortener

Simple URL shortener. FastAPI, Uvicorn, Redis, Docker.

# Run
```bash
cd src
uvicorn app.main:app
# for on-the-fly update server after source code editing.
uvicorn app.main:app --reload
```

# Test
```bash
# from any directory
pytest
```