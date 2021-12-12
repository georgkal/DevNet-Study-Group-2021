FROM python
WORKDIR /home/ubuntu
COPY ./sample-app.py /home/ubuntu/sample-app.py
COPY ./requirements.txt /home/ubuntu/requirements.txt
RUN pip3 install -r /home/ubuntu/requirements.txt
CMD python /home/ubuntu/sample-app.py
EXPOSE 8081
