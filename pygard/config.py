from pydantic import BaseSettings, Field

class AppConfig(BaseSettings):
    git_repo_url: str = Field(..., env="GIT_REPO_URL")
    cache_dir: str = Field("~/.pygard/cache", env="CACHE_DIR")

    class Config:
        env_file = ".env"
