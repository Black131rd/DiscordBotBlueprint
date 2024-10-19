FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]