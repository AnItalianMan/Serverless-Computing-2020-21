#!/bin/sh

# Create Rabbitmq user
( sleep 10 ; \
rabbitmqctl add_user adm serverlessistheway ; \
rabbitmqctl set_user_tags adm administrator ; \
rabbitmqctl set_permissions -p / adm  ".*" ".*" ".*" ; \
rabbitmqctl add_user anitalianman serverlessistheway ; \
rabbitmqctl set_user_tags anitalianman administrator ; \
rabbitmqctl set_permissions -p / anitalianman  ".*" ".*" ".*" ; \
rabbitmqctl add_user admin serverlessistheway ; \
rabbitmqctl set_user_tags admin administrator ; \
rabbitmqctl set_permissions -p / admin  ".*" ".*" ".*" ; \
rabbitmqctl add_user administrator serverlessistheway ; \
rabbitmqctl set_user_tags administrator administrator ; \
rabbitmqctl set_permissions -p / administrator  ".*" ".*" ".*" ; )&

rabbitmq-server
