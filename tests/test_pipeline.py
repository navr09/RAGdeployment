from rag_pipeline.retriever import Retriever
from rag_pipeline.generator import Generator
from rag_pipeline.pipeline import RAGPipeline

def test_rag_pipeline():
    docs = [
        "Employees can access internal documentation through Confluence.",
        "We use Jira for project tracking."
    ]
    pipeline = RAGPipeline(Retriever(docs), Generator())
    answer = pipeline("Where can I find internal documentation?")
    assert "Confluence" in answer
