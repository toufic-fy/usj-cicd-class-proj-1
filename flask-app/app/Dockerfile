FROM python:3.9-slim
# complete the flask service's docker file
# don't forget to add the dependecies to requirements.txt

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]