FROM python:3.6


WORKDIR /usr/local/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
