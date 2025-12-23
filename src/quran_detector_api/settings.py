from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="QD_API_", env_file=".env", extra="ignore")

    host: str = Field(default="127.0.0.1")
    port: int = Field(default=8000, ge=1, le=65535)
    workers: int = Field(default=1, ge=1, le=32)
    log_level: str = Field(default="info")
    cors_origins: str = Field(default="*")
    root_path: str = Field(default="")
    docs_enabled: bool = Field(default=True)
    max_text_length: int = Field(default=5000, ge=1, le=5000)
    max_body_bytes: int = Field(default=65536, ge=1024, le=1048576)

    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache(maxsize=1)
def get_settings() -> ApiSettings:
    return ApiSettings()
