FROM python:3.8.2-buster
COPY . .
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN apt update -y && apt-get install -y software-properties-common && \
    apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main' && apt update -y && \
    apt-get install -y openjdk-11-jdk-headless && \
    export JAVA_HOME && \
    apt-get clean


# START WEBAPP SERVICE
CMD [ "python", "hello_java.py" ]

