# app/config/settings.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_serializer, computed_field
from pathlib import Path
from typing import Literal
import re


class Settings(BaseSettings):
    """
    Application settings loaded from .env file.
    
    Security: Use get_safe_dict() for logging/display.
    Direct field access returns raw values (needed for DB connection).
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # ============================================
    # APP CONFIGURATION
    # ============================================
    app_name: str = "Data Normalizer API"
    app_version: str = "1.0.0"
    debug: bool = False
    environment: Literal["development", "staging", "production"] = "development"

    # ============================================
    # DATABASE CONFIGURATION (SENSITIVE)
    # ============================================
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/data_normalizer"
    database_echo: bool = False

    # ============================================
    # FILE HANDLING
    # ============================================
    max_upload_size_mb: int = 50
    allowed_extensions: str = "csv,xlsx,xls,json"
    upload_dir: str = "data/uploads"
    output_dir: str = "data/outputs"

    # ============================================
    # PROCESSING CONFIGURATION
    # ============================================
    chunk_size: int = 10000
    max_workers: int = 4

    # ============================================
    # SERVER
    # ============================================
    host: str = "0.0.0.0"
    port: int = 8000

    # ============================================
    # COMPUTED FIELDS (Pydantic v2 way)
    # ============================================
    @computed_field  # type: ignore[misc]
    @property
    def max_upload_size_bytes(self) -> int:
        """Convert MB to bytes."""
        return self.max_upload_size_mb * 1024 * 1024

    @computed_field  # type: ignore[misc]
    @property
    def allowed_extensions_list(self) -> list[str]:
        """Convert comma-separated string to list."""
        return [ext.strip().lower() for ext in self.allowed_extensions.split(",")]

    @computed_field  # type: ignore[misc]
    @property
    def is_production(self) -> bool:
        """Check if running in production."""
        return self.environment == "production"

    @computed_field  # type: ignore[misc]
    @property
    def is_development(self) -> bool:
        """Check if running in development."""
        return self.environment == "development"

    # ============================================
    # SECURITY - SAFE DICT FOR LOGGING
    # ============================================
    @staticmethod
    def _mask_url(url: str) -> str:
        """Mask password in database URL."""
        if "@" not in url:
            return url
        return re.sub(r"(://[^:]+:)[^@]+(@)", r"\1****\2", url)

    def get_safe_dict(self) -> dict:
        """
        Return safe dictionary with masked sensitive values.
        Use this for logging and display ONLY.
        """
        data = self.model_dump()
        
        # Mask database_url
        if "database_url" in data:
            data["database_url"] = self._mask_url(data["database_url"])
        
        return data

    def get_safe_display(self) -> str:
        """Return safe string for logging."""
        safe = self.get_safe_dict()
        lines = [f"  {k}: {v}" for k, v in safe.items()]
        return f"Settings(\n" + "\n".join(lines) + "\n)"

    # ============================================
    # PATH HELPERS
    # ============================================
    def get_upload_path(self) -> Path:
        """Get absolute path for uploads directory."""
        path = Path(self.upload_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path

    def get_output_path(self) -> Path:
        """Get absolute path for outputs directory."""
        path = Path(self.output_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path


# ============================================
# SINGLETON INSTANCE
# ============================================
def get_settings() -> Settings:
    """Dependency injection friendly settings getter."""
    return Settings()


settings = Settings()
