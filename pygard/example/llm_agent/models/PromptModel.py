from pydantic import BaseModel, Field

class PromptModel(BaseModel):
    task: str = Field(..., description="Description of the task to be performed")
    state: str = Field(..., description="The state for which information is requested")
    country: str = Field(..., description="The country of the state")

    class Config:
        schema_extra = {
            "example": {
                "task": "Provide information about the population in CA state in USA and the CA size in miles and popular landscapes in CA.",
                "state": "CA",
                "country": "USA"
            }
        }
