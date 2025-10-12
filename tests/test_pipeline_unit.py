import pytest
from rag_pipeline.retriever import Retriever
from rag_pipeline.generator import Generator
from rag_pipeline.pipeline import RAGPipeline

def test_retriever_returns_relevant_docs():
    docs = [
        "Employees can access internal documentation via Confluence.",
        "We use Jira for project management."
    ]
    retriever = Retriever(docs)
    query = "Where is the internal documentation?"
    results = retriever.retrieve(query)
    assert len(results) > 0
    assert "Confluence" in results[0]

def test_generator_returns_answer():
    generator = Generator()
    context = "Employees can access internal documentation via Confluence."
    question = "Where is the internal documentation?"
    answer = generator.generate(context, question)
    assert isinstance(answer, str)
    assert len(answer) > 0

def test_rag_pipeline_end_to_end():
    docs = [
        "Employees can access internal documentation via Confluence.",
        "We use Jira for project management."
    ]
    pipeline = RAGPipeline(Retriever(docs), Generator())
    query = "Where is the internal documentation?"
    answer = pipeline(query)
    assert "Confluence" in answer
