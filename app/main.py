import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import upload, status, result
from app.config.settings import settings

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# App Factory
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers Mount Karo
app.include_router(upload.router)
app.include_router(status.router)
app.include_router(result.router)

@app.get("/")
async def root():
    return {
        "message": "Data Normalizer API is running!",
        "docs": "/docs"
    }
