# RAGdeployment
Using this project to deploy a simple RAG application with MLFlow capabilities, Docker containers and AWS instance

To run the docker image
docker build -t ragapi:latest .
docker run -p 8000:8000 ragapi:latest

Use this curl request to get response
curl -X POST "http://0.0.0.0:8000/predict"      -H "Content-Type: application/json"      -d '{"query":"Where can I find internal documentation?"}'

Building Docker image using github actions was not possible as Github actions only 14-16GB storage. Hence, 
we copy the entire project to EC2 and build the image there. 