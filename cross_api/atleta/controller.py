from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, status, Body, HTTPException, Query
from typing import Optional
from pydantic import UUID4

from cross_api.contrib.dependencies import DatabaseDependency
from cross_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from cross_api.atleta.models import AtletaModel
from cross_api.categorias.models import CategoriaModel
from cross_api.centro_treinamento.models import CentroTreinamentoModel
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_paginate

router = APIRouter()

@router.post('/',
             summary='Criar um novo atleta',
             status_code=status.HTTP_201_CREATED,
             response_model=AtletaOut)
async def post(
        db_session: DatabaseDependency,
        atleta_in: AtletaIn = Body(...)):

    nome_categoria = atleta_in.categoria.nome
    nome_centroTreinamento = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=nome_categoria))
                 ).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Erro!! Categoria {nome_categoria} não encontrada'
        )

    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=nome_centroTreinamento))
                 ).scalars().first()

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Erro!! Centro de Treinamento {nome_categoria} não encontrado'
        )

    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
    except IntegrityError:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f'Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}'
        )
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Ocerreu um erro ao inserir os dados no banco'
        )

    return atleta_out


@router.get('/',
            summary='Consultar todos os Atletas',
            status_code=status.HTTP_200_OK,
            response_model=list[AtletaOut]
            )
async def query(db_session: DatabaseDependency,
                nome: Optional[str] = Query(None, description='Filtrar por nome do atleta'),
                cpf: Optional[str] = Query(None, description='Filtrar por CPF do atleta')
) -> Page[AtletaOut]:

    query_statement = select(AtletaModel)

    if nome:
        query_statement = query_statement.filter(AtletaModel.nome.ilike(f'%{nome}%'))

    if cpf:
        query_statement = query_statement.filter(AtletaModel.cpf == cpf)

    pagina_atletas = await sqlalchemy_paginate(db_session, query_statement)

    pagina_atletas.items = [
        AtletaOut(
           nome=atleta.nome,
           centro_treinamento=atleta.centro_treinamento.nome if atleta.centro_treinamento else None,
           categoria=atleta.categoria.nome if atleta.categoria else None
        )

       for atleta in pagina_atletas.items
    ]

    return pagina_atletas


@router.get('/{id}',
            summary='Consulta um Atleta por id',
            status_code=status.HTTP_200_OK,
            response_model=AtletaOut
            )
async def get(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado para o id: {id}'
        )
    return atleta


@router.patch('/{id}',
              summary='Editar um Atleta pelo id',
              status_code=status.HTTP_200_OK,
              response_model=AtletaOut
              )
async def get(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado para o id: {id}'
        )

    atleta_update = atleta_up.model_dump(exclude_unset=True)

    for key, value, in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)

    return atleta


@router.delete('/{id}',
               summary='Deletar um atleta pelo id',
               status_code=status.HTTP_204_NO_CONTENT,
             )
async def get(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado para o id: {id}'
        )

    await db_session.delete(atleta)
    await db_session.commit()