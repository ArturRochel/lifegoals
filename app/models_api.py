from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional
from datetime import datetime

class ModeloSubObjetivoEntrada(BaseModel):
    titulo: str = Field(..., description="Titulo do sub-objetivo")
    descricao: Optional[str] = None
    concluido: bool = False

class ModeloObjetivoEntrada(BaseModel):
    titulo: str = Field(..., description="Titulo do objetivo")
    descricao: Optional[str] = None
    valor_necessario: Decimal = Field(..., gt=0)
    valor_atual: Decimal = Field(default=Decimal("0"))
    categoria: Optional[str]
    prioridade: str = "media"
    sub_objetivos: list[ModeloSubObjetivoEntrada] = []
    imagem_capa: Optional[str] = None

class ModeloObjetivoSaida(BaseModel):
    id: int = Field(..., description="Chave primaria do objetivo")
    titulo: str = Field(..., description="Titulo do objetivo")
    descricao: Optional[str] = None
    valor_necessario: Decimal = Field(..., gt=0)
    valor_atual: Decimal = Field(default=Decimal("0"))
    categoria: Optional[str]
    prioridade: str = "media"
    progresso: Decimal = Field(default=Decimal("0"))
    sub_objetivos: list[ModeloObjetivoEntrada] = []
    criado_em: datetime
    atualizado_em: datetime
    imagem_capa: Optional[str] = None

class ModeloSubObjetivoSaida(BaseModel):
    id: int = Field(..., description="Chave primária do sub-objetivo")
    titulo: str = Field(..., description="Titulo do sub-objetivo")
    descricao: Optional[str] = None
    concluido: bool = False
    criado_em: datetime
    atualizado_em: datetime