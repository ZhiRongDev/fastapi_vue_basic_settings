import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

from app.routers import api_router
from app.config import settings

# 創建 FastAPI 應用
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# **1. 確保 API 路由優先處理**
app.include_router(api_router, prefix=settings.API_V1_STR)

# **2. 只處理前端路由，避免影響 API**
frontend_dist = Path("frontend/dist")
app.mount("/assets", StaticFiles(directory=frontend_dist / "assets"), name="assets")

@app.get("/{full_path:path}")
async def catch_all(full_path: str, request: Request):
    requested_file = frontend_dist / full_path

    # 如果請求的是 API，不攔截
    if request.url.path.startswith(settings.API_V1_STR):
        return {"error": "API route not found"}

    # 如果是靜態文件，直接返回
    if requested_file.exists() and requested_file.is_file():
        return FileResponse(requested_file)

    # 其他情況返回 Vue 前端的 index.html
    return FileResponse(frontend_dist / "index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, ssl_keyfile="app/cert/snakeoil.key", ssl_certfile="app/cert/snakeoil.crt")