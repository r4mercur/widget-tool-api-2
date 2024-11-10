# syntax=docker/dockerfile:1

FROM python:3.8-buster
RUN apt-get install -y default-libmysqlclient-dev

# Set git config
RUN git config --system core.autocrlf true

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000


#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["flask", "run"]