# tests/unit/test_settings.py

import pytest
from pathlib import Path
from app.config.settings import settings


def test_upload_path():
    """Check karein ke path sahi ban raha hai."""
    upload = settings.get_upload_path()
    assert upload == Path("data/uploads")


def test_database_url_safe():
    """DB URL check - SAFE display use karo."""
    
    # ✅ Safe way - masked
    safe = settings.get_safe_dict()
    print(f"\nSafe DB URL: {safe['database_url']}")
    
    # Password masked hona chahiye
    assert "****" in safe["database_url"]
    
    # Internal check - raw value (DB connect ke liye)
    assert "datanormalizer" in settings.database_url


def test_safe_display():
    """Poora settings safe display."""
    display = settings.get_safe_display()
    print(f"\n{display}")
    
    # Password masked hona chahiye
    assert "****" in display
    # Admin123 nahi dikhna chahiye
    assert "Admin123" not in display


def test_allowed_extensions():
    """Extensions list check."""
    exts = settings.allowed_extensions_list
    print(f"\nExtensions: {exts}")
    assert "csv" in exts
    assert "xlsx" in exts


def test_max_upload_size_bytes():
    """Byte conversion check."""
    bytes_size = settings.max_upload_size_bytes
    print(f"\nMax size: {settings.max_upload_size_mb}MB = {bytes_size} bytes")
    assert bytes_size == 50 * 1024 * 1024


def test_environment_flags():
    """Environment flags check."""
    print(f"\nIs Dev: {settings.is_development}")
    print(f"Is Prod: {settings.is_production}")
    assert settings.is_development is True
