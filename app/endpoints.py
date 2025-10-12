# from fastapi import APIRouter
# from pydantic import BaseModel
# import mlflow.pyfunc
# from app.config import MODEL_PATH

# router = APIRouter()
# model = mlflow.pyfunc.load_model(MODEL_PATH)

# class Query(BaseModel):
#     query: str

# @router.post("/predict")
# def predict(query: Query):
#     answer = model.predict({"query": query.query})
#     return {"answer": answer}

from fastapi import APIRouter
from pydantic import BaseModel
from rag_pipeline.retriever import Retriever
from rag_pipeline.generator import Generator
from rag_pipeline.pipeline import RAGPipeline

router = APIRouter()

# Load docs and initialize pipeline directly
with open("data/documents.txt", "r") as f:
    docs = [line.strip() for line in f.readlines()]

retriever = Retriever(docs)
generator = Generator()
model = RAGPipeline(retriever, generator)

class Query(BaseModel):
    query: str

@router.post("/predict")
def predict(query: Query):
    answer = model(query.query)
    return {"answer": answer}
