from fastapi import APIRouter

import app.schemas as schemas
import app.utils as utils

router = APIRouter()


@router.get("/ping")
async def ping():
    """Check if server is still alive"""
    return {"ping": "pong"}


@router.post("/api/{url}", response_model=schemas.Url)
async def create_url(url: str):
    """Create short url by given url and return it"""
    return utils.create_url(url)


@router.get("/{short_url}", response_model=schemas.Url)
async def get_url(short_url: str):
    """Get full url by short url"""
    return utils.get_url(short_url)


@router.put("/{short_url}", response_model=schemas.Url)
async def delete_url(short_url: str):
    """Delete short url from database"""
    return utils.delete_url(short_url)
