FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean \
&& apt-get install gunicorn3 -y \
&& apt-get install python3.9-dev -y \
&& apt-get install libcurl4-gnutls-dev librtmp-dev -y \
&& apt-get install libnss3 libnss3-dev -y
RUN touch /var/log/flushapp.log
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt
RUN python classification/setup.py
COPY . /backend/
EXPOSE 3000
