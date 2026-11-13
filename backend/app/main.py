from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AP Trading Control"
    environment: str = "development"
    live_trading_enabled: bool = False
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
app = FastAPI(title=settings.app_name, version="0.1.0")

# Local development only. Restrict origins before exposing this service publicly.
app.add_middleware(CORSMiddleware, allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"], allow_credentials=False, allow_methods=["GET"], allow_headers=["*"])

@app.get("/api/health", tags=["system"])
def health():
    return {"status": "ok", "environment": settings.environment, "live_trading_enabled": False}

@app.get("/api/readiness", tags=["system"])
def readiness():
    return {"ready": True, "mode": "local-development", "execution": "disabled", "live_trading_enabled": False}
