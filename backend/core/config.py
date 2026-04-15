from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # LLM
    llm_provider: Literal["groq", "gemini", "ollama"] = "groq"
    llm_model: str = "llama-3.3-70b-versatile"
    groq_api_key: str = Field(default="", repr=False)  # repr=False hides from logs
    gemini_api_key: str = Field(default="", repr=False)
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    # App
    app_env: Literal["development", "production", "test"] = "development"
    log_level: str = "INFO"
    database_url: str = "sqlite+aiosqlite:///./ikman_agent.db"

    # Search
    max_search_results: int = 20
    top_n_default: int = 5
    llm_requests_per_minute: int = 20
    scraper_delay_seconds: float = 1.5

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

