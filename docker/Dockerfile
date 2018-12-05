#Grab the latest alpine image
FROM alpine:latest

MAINTAINER Sergi Torrellas

# Add folder
RUN apk add --no-cache --update python3 bash
ADD . /repo/
WORKDIR /repo/
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations ui
RUN python3 manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" \
          | python3 manage.py shell


EXPOSE 8000

# Run container
CMD python3 /repo/manage.py runserver 0.0.0.0:$PORT
#sudo docker run -t -p8000:8000 idrink
