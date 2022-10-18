# Set base image (host OS)
FROM python:3.9.12

# File Author / Maintainer
MAINTAINER Gabriel Da Costa

#add project files to the code/ folder
ADD . /code

# Setup the working directory in the container
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code
RUN pip install -r requirements.txt

# Define the default port and block access for other applications
EXPOSE 8000

# Setup the executable command in the container
CMD python manage.py runserver 0.0.0.0:8000
