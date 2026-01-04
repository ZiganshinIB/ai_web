from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).parent.parent.parent
BASE_DIR = Path(__file__).parent.parent


class UnsplashConfig(BaseModel):
    ID: int
    ACCESS_KEY: SecretStr
    SECRET_KEY: SecretStr
    MAX_CONNECTIONS: int | None = Field(None, gt=0)
    TIMEOUT: int = Field(default=20, gt=0)

    model_config = ConfigDict(
        use_attribute_docstrings=True,
    )


class AIConfig(BaseModel):
    API_KEY: SecretStr
    MAX_CONNECTIONS: int | None = Field(None, gt=0)
    BASE_URL: HttpUrl = HttpUrl("https://bothub.chat/api/v2/openai/v1/chat/completions")
    MODEL: str = "gpt-3.5-turbo"  # ? Нужно ли, так как BotHub поддерживает различныенные модели?

    model_config = ConfigDict(
        use_attribute_docstrings=True,
    )


class Settings(BaseSettings):
    DEBUG: bool = False
    AI: AIConfig
    UNSPLASH: UnsplashConfig

    model_config = SettingsConfigDict(
        env_file=PROJECT_DIR / ".env",
        case_sensitive=False,  # Без регистра
        env_nested_delimiter="__",  # Разделитель
        # env_prefix="APP_CONFIG__",
        use_attribute_docstrings=True,
    )


settings = Settings()
