FROM python:3.8.3 as builder

RUN apt-get update



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# set work directory
WORKDIR /app

# copy requirements
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]