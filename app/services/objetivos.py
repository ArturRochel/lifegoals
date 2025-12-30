from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timezone
from sqlmodel import Session, select
from app.models_db.objetivo import Objetivo
from app.models_api import ModeloObjetivoEntrada
from typing import Sequence

def calcular_progresso(valor_atual: Decimal, valor_necessario: Decimal) -> Decimal:
    if valor_necessario == 0:
        return Decimal("0")
    bruto = (valor_atual / valor_necessario) * Decimal("100")
    return bruto.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def criar_objetivo(session: Session, dados: ModeloObjetivoEntrada) -> Objetivo:
    objetivo = Objetivo(
        titulo= dados.titulo,
        descricao= dados.descricao,
        valor_necessario= dados.valor_necessario,
        valor_atual= dados.valor_atual,
        categoria= dados.categoria,
        prioridade= dados.prioridade,
        imagem_capa= dados.imagem_capa
    )

    objetivo.progresso = calcular_progresso(objetivo.valor_atual, objetivo.valor_necessario)

    agora = datetime.now(timezone.utc)
    objetivo.criado_em = agora
    objetivo.atualizado_em = agora

    session.add(objetivo)
    session.commit()
    session.refresh(objetivo)
    return objetivo

def listar_objetivos(session: Session) -> Sequence[Objetivo]:
    consulta = select(Objetivo)
    resultados = session.exec(consulta).all()
    return resultados