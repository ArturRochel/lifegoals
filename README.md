# Life Goals 🎯

Life Goals é um sistema web pessoal criado para **monitorar metas e objetivos para o ano de 2026**.

O projeto segue uma arquitetura **full stack**, com front-end em **React + Tailwind CSS** e back-end em **Python**, utilizando **FastAPI** e **SQLModel**.

> Este sistema foi pensado para uso pessoal, mas seguindo boas práticas de desenvolvimento.

---

## 🧠 Tecnologias utilizadas

### Front-end
- React
- Tailwind CSS

### Back-end
- Python 3.14+
- FastAPI
- Uvicorn
- SQLModel
- Alembic
- Pydantic

### Banco de dados
- SQLite (ambiente local)
- Estrutura preparada para outros bancos (PostgreSQL, MySQL)

---

## 📁 Estrutura inicial do projeto

```text
life-goals/
├── app/                # Código do back-end (FastAPI)
│   ├── main.py
│   ├── database.py
│   └── models/
├── alembic/            # Migrations do banco
│   └── versions/
├── alembic.ini
├── requirements.txt
├── README.md
└── .gitignore

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
