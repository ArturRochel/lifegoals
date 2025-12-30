from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timezone



class Objetivo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str = Field(index=True, nullable=False)
    descricao: str | None = None
    valor_necessario: Decimal = Field(nullable=False)
    valor_atual: Decimal = Field(nullable=False)
    progresso: Decimal = Field(default=Decimal("0")) 
    categoria: str | None = None
    prioridade: str = Field(default="media", nullable=False)
    criado_em: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    atualizado_em: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    imagem_capa: str | None = None
