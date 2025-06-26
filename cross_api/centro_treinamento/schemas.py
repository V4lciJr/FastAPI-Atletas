from typing import Annotated
from pydantic import Field, PositiveFloat
from cross_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Cobra Kai", max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do centro de treinamento', example='Rua Augusta', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario do centro', example='Miguel Domingues', max_length=30)]