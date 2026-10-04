import os
import sys

# Ensure both api folder and root folder are on sys.path
api_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(api_dir)

for p in [api_dir, root_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from backend.main import app
except Exception:
    try:
        from api.backend.main import app
    except Exception as e:
        import traceback
        from fastapi import FastAPI
        from fastapi.responses import JSONResponse

        app = FastAPI(title="SENTINEL-X Diagnostic")

        @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
        async def diagnostic_error_handler(path: str = ""):
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Failed to initialize SENTINEL-X backend",
                    "exception": str(e),
                    "traceback": traceback.format_exc(),
                    "sys_path": sys.path,
                    "cwd": os.getcwd()
                }
            )
