FROM python:3.9-slim

WORKDIR /djangonautic

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN apt update
RUN apt install build-essential -y
RUN pip install -r requirements.txt

COPY . .

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn djangonautic.wsgi:application --bind 0.0.0.0:$PORT