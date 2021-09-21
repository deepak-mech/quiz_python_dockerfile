FROM  centos

RUN   yum install python3 -y

RUN   mkdir -p /home/app

WORKDIR  /home/app

COPY  ./app  /home/app

CMD   ["python3", "assignment.py"]
