from pydantic import BaseModel, Field

class ResponseModel(BaseModel):
    population: str = Field(..., description="Population of the state")
    size: str = Field(..., description="Size of the state in miles")
    landscapes: list[str] = Field(..., description="Popular landscapes in the state")

    class Config:
        schema_extra = {
            "example": {
                "population": "39.14 million",
                "size": "163,696 square miles",
                "landscapes": ["Yosemite National Park", "Death Valley", "Big Sur"]
            }
        }
