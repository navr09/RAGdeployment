import mlflow
from mlflow.tracking import MlflowClient
from rag_pipeline.mlflow_model import RAGMLflowWrapper

mlflow.set_experiment("RAGExperiment")

# Log model
with mlflow.start_run() as run:
    mlflow.pyfunc.log_model(
        artifact_path="RAGPipeline",
        python_model=RAGMLflowWrapper(),
        registered_model_name="RAGPipeline"
    )

# Create alias AFTER registration
client = MlflowClient()

# Get the latest version number
latest_version = client.get_latest_versions("RAGPipeline")[0].version

# Assign alias “production”
client.set_model_version_alias(
    name="RAGPipeline",
    version=latest_version,
    alias="production"
)

print(f"✅ Model version {latest_version} logged and aliased as 'production'.")
