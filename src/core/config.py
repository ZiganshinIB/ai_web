from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).parent.parent.parent
BASE_DIR = Path(__file__).parent.parent


class UnsplashConfig(BaseModel):
    id: int | None = Field(None, gt=0)
    '''ID приложения'''
    access_key: SecretStr
    '''Ключ доступа'''
    secret_key: SecretStr
    '''Секретный ключ'''
    max_connections: int | None = Field(None, gt=0)
    '''Количество подключений'''
    timeout: int = Field(20, gt=0)
    '''Время ожидания в секундах'''

    model_config = ConfigDict(
        use_attribute_docstrings=True,
    )


class AIConfig(BaseModel):
    api_key: SecretStr
    '''Ключ доступа'''
    max_connections: int | None = Field(None, gt=0)
    '''Количество подключений'''
    base_url: HttpUrl = HttpUrl("https://bothub.chat/api/v2/openai/v1/chat/completions")
    '''Базовый URL'''
    model: str = "deepseek-chat-v3-0324"
    '''Модель нейронной сети'''

    model_config = ConfigDict(
        use_attribute_docstrings=True,
    )


class Settings(BaseSettings):
    debug: bool = False
    '''режим работы программы'''
    ai: AIConfig
    '''Конфигурация AI'''
    unsplash: UnsplashConfig
    '''Конфигурация Unsplash'''

    model_config = SettingsConfigDict(
        env_file=PROJECT_DIR / ".env",
        case_sensitive=False,  # Без регистра
        env_nested_delimiter="__",  # Разделитель
        use_attribute_docstrings=True,
    )


settings = Settings()
