# sudo docker build -t finddocker .
# sudo docker run -it -p 8080:5000 -v .:/data finddocker bash
# docker-compose run web
FROM debian
#FROM python:3.4.2

# Get basics
RUN apt-get update
RUN apt-get -y upgrade
#RUN apt-get install -y golang git wget curl vim
RUN apt-get install -y libgeos++ binutils libproj-dev gdal-bin curl htop python3-pip python3-gdal python3-jinja2
RUN pip3 install django
#RUN mkdir /usr/local/work
#ENV GOPATH /usr/local/work

ADD . /code/

# Add Python stuff
#RUN apt-get install -y python3 python3-dev python3-pip
#RUN apt-get install -y python3-scipy python3-numpy
#RUN python3 -m pip install scikit-learn

# Install FIND
WORKDIR "/root"
#RUN go get github.com/schollz/find
#RUN git clone https://github.com/schollz/find.git
#WORKDIR "/root/find"
#RUN go build
#RUN echo "\ninclude_dir /root/find/mosquitto" >> /etc/mosquitto/mosquitto.conf

# Startup
#CMD ["/usr/bin/supervisord"]
