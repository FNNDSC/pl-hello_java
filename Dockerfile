FROM openjdk
WORKDIR /usr/local/src
COPY . .
ENTRYPOINT ["java","HelloWorld"]

