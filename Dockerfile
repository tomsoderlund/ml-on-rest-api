FROM python:3.10

ENV PYTHONBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME

RUN pip install transformers[torch] Flask gunicorn


COPY . ./

EXPOSE 5000
ENV PORT 5000

ENV GOOGLE_ENTRYPOINT gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

