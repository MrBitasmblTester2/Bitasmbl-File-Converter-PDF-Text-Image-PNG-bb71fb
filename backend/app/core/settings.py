from pydantic import BaseSettings
class Settings(BaseSettings):
    backend_cors_origins: list[str] = ["*"]
settings = Settings()