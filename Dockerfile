FROM python:3.9-slim
WORKDIR /app
COPY fixedwidthfile.py .
CMD ["python", "fixedwidthfile.py"]
