import random
import string

from fastapi import HTTPException, status

from app.redis_helper import RedisClient


def generate_short_url(url):
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


def create_url(url):
    redis_conn = RedisClient().conn
    short_url = generate_short_url(url)
    redis_conn.set(short_url, url)
    return {"short_url": short_url, "url": url}


def get_url(short_url):
    redis_conn = RedisClient().conn
    url = redis_conn.get(short_url)
    if url is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid short url",
        )
    return {"short_url": short_url, "url": url}


def delete_url(short_url):
    redis_conn = RedisClient().conn
    url = redis_conn.get(short_url)
    if url is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid short url",
        )
    redis_conn.delete(short_url)
    return {"short_url": short_url, "url": url}
