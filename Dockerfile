FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      libpq-dev \
      curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root

COPY . .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]