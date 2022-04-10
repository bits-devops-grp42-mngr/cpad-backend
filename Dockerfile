FROM python:3.5.7
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app
EXPOSE 8000
VOLUME ["/app-data"]
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000