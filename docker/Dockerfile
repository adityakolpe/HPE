FROM ubuntu

RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requierments.txt

COPY . /app

EXPOSE 5000
CMD ["python", "/app/main.py"]
