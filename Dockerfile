FROM python:3.9-slim

# Setup the working directory 
WORKDIR /app

# Copy the script to the container 
COPY IPStack_API_Query.py . 

# Specify the entrypoint 
ENTRYPOINT ["python3", "IPStack_API_Query.py"]

