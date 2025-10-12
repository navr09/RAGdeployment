import mlflow.pyfunc

class RAGMLflowWrapper(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        from rag_pipeline.pipeline import RAGPipeline
        from rag_pipeline.retriever import Retriever
        from rag_pipeline.generator import Generator
        
        with open("data/documents.txt", "r") as f:
            docs = [line.strip() for line in f.readlines()]
        self.pipeline = RAGPipeline(Retriever(docs), Generator())

    def predict(self, context, model_input):
        query = model_input["query"]
        return self.pipeline(query)

