FROM python:3.10.5

WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt