FROM python:2-alpine

RUN pip install markdown && pip install docopt && pip install mdv html2text requests beautifulsoup4

ENV URL_PARTERN=https://hub.docker.com/r/#IMAGE#/
ENV CONTENT_SELECTOR=div[data-reactid*=.2.1.1.0.0.0.0.0.1.1.0.1]

ADD image_help.py /image_help.py
ENTRYPOINT ["python", "/image_help.py"]
