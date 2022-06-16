FROM python:3.8.13

WORKDIR /app

COPY . .

EXPOSE 8501

RUN python3 -m pip install -r requirements.txt

CMD ["streamlit","run", "app.py"]
