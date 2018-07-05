FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY . /test_blog/
WORKDIR /test_blog/
RUN pip3 install virtualenv virtualenvwrapper
RUN virtualenv env
RUN /bin/bash -c "source /test_blog/env/bin/activate"
ADD requirements.txt /test_blog/
RUN pip3 install -r requirements.txt
ADD . /test_blog/ 

EXPOSE 8000
