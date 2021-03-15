FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
WORKDIR /usr/src/count_app
COPY count_app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENV FLASK_APP=./count_app.py
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
# ENTRYPOINT ["python3", "./count_app.py", "--host=0.0.0.0"]
EXPOSE 5000
