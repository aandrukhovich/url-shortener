import uvicorn
from fastapi import FastAPI

import app.redis_helper
import app.redis_helper as redis_helper
import app.routes as routes

app = FastAPI()
app.include_router(routes.router)


@app.on_event("startup")
async def startup():
    redis_helper.startup()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
