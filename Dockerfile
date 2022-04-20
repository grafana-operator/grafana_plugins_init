FROM registry.access.redhat.com/ubi8/python-39

COPY plugins.py ./

CMD [ "python", "./plugins.py"]
