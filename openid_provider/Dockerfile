FROM python:3.11.0b1-alpine

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

# ENTRYPOINT [ "flask" ]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

