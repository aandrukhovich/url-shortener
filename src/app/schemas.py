from pydantic import BaseModel


class Url(BaseModel):
    url: str
    short_url: str
