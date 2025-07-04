from fastapi import APIRouter, status, Body
from cross_api.contrib.dependencies import DatabaseDependency
from cross_api.atleta.schemas import AtletaIn

router = APIRouter()

@router.post('/',
             summary='Criar novo atleta',
             status_code=status.HTTP_201_CREATED)
async def post(
        db_session: DatabaseDependency,
        atleta_in: AtletaIn = Body(...)):
    pass