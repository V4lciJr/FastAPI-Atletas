from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from cross_api.categorias.schemas import CategoriaIn
from cross_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from cross_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="Manoel", max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=35)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=78.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.76)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass


class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Manoel', max_length=50)]
    idade: Annotated[Optional[str], Field(None, description='Idade do atleta', example='44')]
