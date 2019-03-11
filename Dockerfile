FROM python:3

COPY plugins.py ./

CMD [ "python", "./plugins.py"]

