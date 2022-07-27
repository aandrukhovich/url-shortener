import uvicorn
from fastapi import FastAPI

import app.routes as routes

app = FastAPI()
app.include_router(routes.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
