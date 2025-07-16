from pydantic import BaseModel, HttpUrl, AnyHttpUrl


class URLRequest(BaseModel):
    url: HttpUrl


class URLResponse(BaseModel):
    short_url: AnyHttpUrl
   