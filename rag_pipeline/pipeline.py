class RAGPipeline:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def __call__(self, query):
        docs = self.retriever.retrieve(query)
        context = " ".join(docs)
        return self.generator.generate(context, query)
