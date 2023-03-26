FROM python:3.10.0a6-buster

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python3", "./main.py"]