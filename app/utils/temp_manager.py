import tempfile
from pathlib import Path

def save_temp_file(file_content, extension: str) -> Path:
    if extension and not extension.startswith('.'):
        extension = f".{extension}"
    with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as tmp:
        tmp.write(file_content)
    return Path(tmp.name)
