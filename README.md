# IP Stack API Query Tool

This tool allows users to query the IP Stack API to retreive details about a specific IP address and return the latitude and longitude associated with it. 

## Prerequisites 
* Docker installed on your system 
* API Key from ipstack.com 

## Setup 
Update the api_key.txt file with your api key 
```bash
vi api_key.txt
```

Build the Docker Image
```bash
docker build -t api_query_tool . 
```

## Usage 
To query information about a specific IP address, run:
```bash
docker run -v $(pwd)/api_key.txt:/tmp/api_key.txt api_query_tool -i <IP_TO_QUERY> --secret_file /tmp/api_key.txt
```

