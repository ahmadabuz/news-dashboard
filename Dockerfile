FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install requests transformers firebase-admin pandas streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true", "--server.enableCORS=false"]
