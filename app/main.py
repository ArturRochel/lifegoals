from fastapi import FastAPI, Depends
from sqlmodel import Session
from app.database import get_session, create_db_and_tables
from app.models_api import ModeloObjetivoEntrada, ModeloObjetivoSaida
from app.services.objetivos import criar_objetivo, listar_objetivos
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/objetivos", response_model= list[ModeloObjetivoSaida], description="Rota para listar objetivos cadastrados")
def listar_objetivos_endpoint(session: Session = Depends(get_session)):
    objetivos = listar_objetivos(session)
    return [
        ModeloObjetivoSaida.model_validate(obj, from_attributes=True)
        for obj in objetivos
    ] 

@app.post("/objetivos", response_model= ModeloObjetivoSaida, description="Rota utilizada para cadastrar objetivos")
def cadastrar_objetivo(dados: ModeloObjetivoEntrada, session: Session = Depends(get_session)):
    objetivo = criar_objetivo(session= session, dados=dados)

    return ModeloObjetivoSaida.model_validate(objetivo, from_attributes=True)