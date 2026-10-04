"""
SENTINEL-X — Root FastAPI Entrypoint
Enables zero-config deployment across Vercel, Render, Railway, and local execution.
"""

import os
import sys

# Ensure root directory is in sys.path
root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from backend.main import app

if __name__ == "__main__":
    import uvicorn
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.main:app", host=host, port=port)
