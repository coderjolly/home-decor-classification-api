FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./


RUN pip3 install -r requirements.txt


COPY . .
EXPOSE 5000

CMD ["python3", "main.py"]