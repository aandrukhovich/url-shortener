import random
import string

import redis
from fastapi import Depends, HTTPException, status


def generate_short_url(url):
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


def create_url(url):
    redis_client = redis.Redis()
    short_url = generate_short_url(url)
    redis_client.set(short_url, url)
    return {"short_url": short_url, "url": url}


def get_url(short_url):
    redis_client = redis.Redis()
    url = redis_client.get(short_url)
    if url is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid short url",
        )
    return {"short_url": short_url, "url": url}
