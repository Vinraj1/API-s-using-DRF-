<<<<<<< HEAD
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /app/tutorial

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# for production 
=======
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /app/tutorial

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# for production 
>>>>>>> ef79b1ff6dcedc869fb8a3aa05a89cc0dc427a68
#CMD ["gunicorn", "projectname.wsgi:application", "--bind", "0.0.0.0:8000"]