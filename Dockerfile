FROM django:1.9.5
WORKDIR /app
EXPOSE 80
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
CMD python manage.py runserver 0.0.0.0:80
