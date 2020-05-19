# Pull base Image
FROM python:3

# MAINTAINER
MAINTAINER "Rajkumar Vijayakumar"
COPY my_script.py /
RUN pip install pystrich
CMD [ "python", "./my_script.py" ]
