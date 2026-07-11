import pytest
from app.core.name_standardizer import standardizer_name
from app.core.schema_detector import detect_column_schema
import pandas as pd

@pytest.mark.asyncio
async def test_root_endpoint(client):
    """Check if API starts and returns welcome message"""
    response = await client.get("/")
    assert response.status_code == 200
    assert "Data Normalizer API" in response.json()["message"]

def test_standardizer_integration():
    """Test the actual standardizer with a dirty string"""
    dirty = "  User FIRST Name  "
    clean = standardizer_name(dirty)
    assert clean == "user_first_name"

def test_schema_detector_integration():
    """Test schema detection on a mini dataframe"""
    df = pd.DataFrame({"age": [1, 2, 3], "name": ["a", "b", "c"]})
    schema = detect_column_schema(df)
    assert schema["age"] == "int"
    assert schema["name"] == "string"
