FROM python:3.7-slim
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

#docker build -t fprintes/catalog .
#docker run -p localhost:8000 -v "/home/felipe/PycharmProjects/flask-data-catalog-gcp:/var/www" -w "/var/www" fprintes/catalog