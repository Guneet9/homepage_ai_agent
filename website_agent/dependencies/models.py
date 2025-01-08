from pydantic import BaseModel, HttpUrl

# Pydantic models
class WebsiteInput(BaseModel):
    url: HttpUrl

class WebsiteOutput(BaseModel):
    industry: str | None
    company_size: str | None
    location: str | None