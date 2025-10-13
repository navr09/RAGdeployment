# RAGdeployment
Using this project to deploy a simple RAG application with MLFlow capabilities, Docker containers and AWS instance

To run the docker image
docker build -t ragapi:latest .
docker run -p 8000:8000 ragapi:latest

Use this curl request to get response
curl -X POST "http://0.0.0.0:8000/predict"      -H "Content-Type: application/json"      -d '{"query":"Where can I find internal documentation?"}'

Building Docker image using github actions was not possible as Github actions only 14-16GB storage. Hence, 
we copy the entire project to EC2 and build the image there. 

This server once created in ec2 mifht not have permissions:
ssh -i mykey.pem ec2-user@50.19.129.160
So add this before and try the above query
chmod 400 mykey.pem


You have to install Docker in Linux server in EC2 instance
ssh -i mykey.pem ec2-user@50.19.129.160

Then run these commands:
# 1️⃣ Update your packages
sudo dnf update -y

# 2️⃣ Install Docker (correct for Amazon Linux)
sudo dnf install docker -y

# 3️⃣ Enable Docker to start on boot
sudo systemctl enable docker

# 4️⃣ Start Docker service now
sudo systemctl start docker

# 5️⃣ Add your EC2 user to the Docker group
sudo usermod -aG docker ec2-user

Afterwards 
exit

THen test if docker is there
ssh -i mykey.pem ec2-user@50.19.129.160

docker ps

You should see this if docker is installed successfully
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS   PORTS   NAMES
