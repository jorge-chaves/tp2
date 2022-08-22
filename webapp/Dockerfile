FROM python:3.7.13-buster

WORKDIR /tmp

RUN pip install -r requirements.txt

ENV DB_HOST=
ENV DB_USER=
ENV DB_PASSWD=

CMD ["python", "app.py"]
