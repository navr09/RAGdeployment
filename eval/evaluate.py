import json
from rag_pipeline.pipeline import RAGPipeline
from rag_pipeline.retriever import Retriever
from rag_pipeline.generator import Generator

def evaluate_pipeline(pipeline, dataset_path="data/qa_dataset.json"):
    with open(dataset_path, "r") as f:
        dataset = json.load(f)

    exact_match = 0
    for item in dataset:
        pred = pipeline(item["question"])
        if pred.strip().lower() == item["answer"].strip().lower():
            exact_match += 1

    return {"exact_match": exact_match / len(dataset)}

if __name__ == "__main__":
    with open("data/documents.txt", "r") as f:
        docs = [line.strip() for line in f.readlines()]

    retriever = Retriever(docs)
    generator = Generator()
    rag_pipeline = RAGPipeline(retriever, generator)

    metrics = evaluate_pipeline(rag_pipeline)
    print("Evaluation metrics:", metrics)
