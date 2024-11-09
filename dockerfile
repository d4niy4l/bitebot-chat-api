FROM python:3.11.0-slim-buster

WORKDIR /server

COPY . /server

RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]


