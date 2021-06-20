FROM openjdk:8-jre-alpine3.9

COPY ./target/logconsumer.jar /logconsumer.jar

ENV RABBIT_USER_USERNAME=adm
ENV RABBIT_USER_PASSWORD=serverlessistheway
ENV RABBIT_QUEUE_NAME=log
ENV RABBIT_HOST=rabbitmq

CMD ["java", "-jar", "/logconsumer.jar"]