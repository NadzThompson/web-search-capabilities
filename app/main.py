import logging
from fastapi import FastAPI
from app.api.routes import router
from app.config import settings
logging.basicConfig(level=getattr(logging, settings.nova_log_level.upper(), logging.INFO))
app = FastAPI(title="NOVA Web Search Agent", version="4.0.0")
app.include_router(router)
