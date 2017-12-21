FROM python:2

ADD requirements.txt /
ADD app.py /
ADD templates/barcode.jinja2 /templates/barcode.jinja2
ADD my_barcode.py /
RUN pip install -r /requirements.txt
CMD [ "python", "/app.py"]

