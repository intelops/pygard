from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pygard.data_model_validator import validate_data
from pygard.utils import logger, ensure_cache_dir
from pygard.git_utils import clone_repo, copy_policies_to_cache
import os

app = FastAPI()

class ValidationRequest(BaseModel):
    models: list[str]
    data: dict

@app.post("/validate/")
async def validate(request: ValidationRequest):
    try:
        # Ensure cache directory exists
        cache_dir = os.path.expanduser("~/.pygard/cache")
        ensure_cache_dir(cache_dir)

        # Clone repo and copy policies
        repo_url = "https://your-git-repo-url.git"
        repo_path = clone_repo(repo_url, cache_dir)
        copy_policies_to_cache(repo_path, cache_dir)

        # Validate data
        validation_results = validate_data(request.models, request.data)
        return {"validation_results": validation_results}
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
