FROM python:3-alpine


RUN mkdir -p /usr/src/http-server
WORKDIR /usr/src/http-server

RUN pip3 install --upgrade pip
RUN pip3 install aiomysql aiohttp mysql-connector-python

COPY . .
CMD ["python3", "main.py"]
