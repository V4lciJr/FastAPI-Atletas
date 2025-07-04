from fastapi import APIRouter
from cross_api.atleta.controller import router as atleta

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])