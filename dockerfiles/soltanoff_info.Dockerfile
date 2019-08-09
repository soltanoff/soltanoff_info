FROM python:3.5
MAINTAINER Ilya Soltanov <piccadillable@gamil.com>
ENV PYTHONBUFFERED 1
COPY ./requirements.txt /soltanoff_info/requirements.txt
COPY ./wait-for-it.sh /soltanoff_info/wait-for-it.sh
WORKDIR /soltanoff_info
RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt
COPY . /soltanoff_info
