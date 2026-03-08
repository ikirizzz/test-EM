FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN useradd -m -u 1001 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]
