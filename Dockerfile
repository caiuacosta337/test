FROM python:3.13-slim

WORKDIR /app

COPY requirements-lock.txt /app/requirements-lock.txt

RUN pip install --no-cache-dir --only-binary :all: --require-hashes -r /app/requirements-lock.txt \
    && pip install --no-cache-dir --only-binary :all: "gunicorn==23.0.0"

COPY app.py /app/
COPY templates/ /app/templates/
COPY static/ /app/static/

RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]