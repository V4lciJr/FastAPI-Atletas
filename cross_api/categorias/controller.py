from uuid import uuid4
from fastapi import APIRouter, status, Body, HTTPException
from pydantic import UUID4

from cross_api.categorias.models import CategoriaModel
from cross_api.contrib.dependencies import DatabaseDependency
from cross_api.categorias.schemas import CategoriaIn, CategoriaOut
from sqlalchemy.future import select

router = APIRouter()


@router.post('/',
             summary='Criar uma nova Categoria',
             status_code=status.HTTP_201_CREATED,
             response_model=CategoriaOut,
             )
async def post(
        db_session: DatabaseDependency,
        categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:

    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out


@router.get('/',
            summary='Consultar todas as categorias',
            status_code=status.HTTP_200_OK,
            response_model=list[CategoriaOut],
            )
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()

    return categorias


@router.get('/{id}',
            summary='Consultar uma categoria pelo id',
            status_code=status.HTTP_200_OK,
            response_model=CategoriaOut,
            )
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))
                               ).scalars().first()

    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Categoria não encontrada no id: {id}')

    return categoria
