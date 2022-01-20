FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /frexcodesafio
WORKDIR /frexcodesafio  
ADD requirements.txt /frexcodesafio/
RUN  pip install -r requirements.txt
ADD . /frexcodesafio/