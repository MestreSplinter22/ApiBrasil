from fastapi import FastAPI, HTTPException
from func.extrairnome import extrair_nome
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/extrairnome/{formatocpf}")
async def get_nome(formatocpf: str):
    try:
        nome = extrair_nome(formatocpf)
        return {"nome": nome}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Partition not found")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
