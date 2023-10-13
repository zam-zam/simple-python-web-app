FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_NO_INTERACTION=1

WORKDIR /

RUN groupadd -g 2000 app \
  && useradd -u 2000 -g 2000 -M -s /bin/sh app

COPY simple_python_web_app/ /simple_python_web_app/

RUN chmod -R a-w /simple_python_web_app/*

WORKDIR /simple_python_web_app
USER app
ENTRYPOINT ["python", "main.py"]
