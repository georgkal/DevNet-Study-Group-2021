FROM python
WORKDIR /home/ubuntu
COPY ./sample-app.py /home/ubuntu/sample-app.py
COPY ./requirements.txt /home/ubuntu/requirements.txt
RUN pip3 install -r /home/ubuntu/requirements.txt
CMD python3 /home/ubuntu/sample-app.py
EXPOSE 8080
