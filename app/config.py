from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",  # Path to the .env file
        env_ignore_empty=True,
        extra="ignore",
    )
    
    """Base configuration shared across all environments."""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    VERSION: str = "1.0.0rc1"
    API_V1_STR: str = "/api/v1"

    ENVIRONMENT: str
    PROJECT_NAME: str

# Select the correct configuration
settings = Settings()