FROM python:3-alpine

COPY plugins.py ./

CMD [ "python", "./plugins.py"]

