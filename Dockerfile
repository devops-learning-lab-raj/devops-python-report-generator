FROM python:3.12-slim
WORKDIR /workspace
COPY app ./app
COPY config ./config
CMD ["python", "app/report.py"]