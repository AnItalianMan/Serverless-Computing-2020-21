FROM python:3.7

ENV BOT_TOKEN=
ENV CHAT_ID=
ENV USERNAME=anitalianman
ENV PASSWORD=serverlessistheway
ENV QUEUE_NAME=alarm

ENV APP_HOME /AlarmConsumer

COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

COPY ./ ./AlarmConsumer

CMD cd AlarmConsumer && python main.py