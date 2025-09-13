import base64
from pathlib import Path

__all__ = ["load_icon"]

def load_icon(path: str, width: int = 20, height: int = 20) -> str:
    file = Path(path)
    data = base64.b64encode(file.read_bytes()).decode()
    mime = "image/svg+xml" if file.suffix == ".svg" else "image/png"
    return (
        f'<img src="data:{mime};base64,{data}" '
        f'width="{width}" height="{height}" style="vertical-align:middle"/>'
    )
