from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import text_audio

app = FastAPI(title="Steganography API", version="1.0.0")

# CORS: allow local Ionic React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8100", "http://127.0.0.1:8100", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(text_audio.router, prefix="/v1", tags=["text-audio"])

@app.get("/health")
def health():
    return {"status": "ok"}
