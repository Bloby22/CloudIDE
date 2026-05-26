import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.terminal import router as terminal_router
 
app = FastAPI(
    title="BlobIDE",
    version="0.1.0",
    description="Custom IDE backend",
)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "tauri://localhost",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
app.include_router(terminal_router, prefix="/api/terminal", tags=["terminal"])
 
 
@app.get("/health", tags=["meta"])
async def health() -> dict:
    return {"status": "ok", "app": "BlobIDE", "version": "0.1.0"}
 
 
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
 