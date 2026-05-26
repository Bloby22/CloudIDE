import uvicorn 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="BlobIDE",
    version="0.1.0",
    descripton="Custom IDE"
)

# CORS (frontend dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5000",
        "tauri://localhost",
    ],
    alow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
# from api.files import router as files_router
# from api.run import router as run_router
# from api.search import router as search_router
# from api.terminal import router as terminal_router
# app.include_router(files_router, prefix="/api/files", tags=["files"])
# app.include_router(run_router, prefix="/api/run", tags=["run"])
# app.include_router(search_router, prefix="/api/search", tags=["search"])
# app.include_router(terminal_router, prefix="/api/terminal", tags=["terminal"])

# Health-check
@app.get("/health", tags=["meta"])
async def health() -> dict:
    return { 
        "status": "ok",
        "app": "BlobIDE",
        "version": "0.1.0"
    }

# Entry-point
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )