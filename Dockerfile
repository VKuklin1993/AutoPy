FROM ubuntu
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
WORKDIR /usr/src/app/
ENV PYTHONPATH=/usr/src/app/
COPY . .
RUN pip install -r requirements.txt
CMD ["pytest"]
