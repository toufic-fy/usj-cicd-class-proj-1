FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# CMD ["flask","run","-h","0.0.0.0","-p","5000"]

CMD [ "python","app.py" ]