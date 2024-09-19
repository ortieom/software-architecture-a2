#!/bin/bash

set -x

# start server
docker-compose -f ../code/docker-compose.yaml up -d

# wait till server starts
sleep 30

# send message and quit
printf "send hi\nquit" | python ../code/client.py

# store the message count
count_value=$(curl 127.0.0.1:8000/messages/count)

# connect to docker container and kill all uvicorn
docker exec code-server-1 pkill uvicorn

sleep 60

# testing restart
ping_status=$(curl -s -o /dev/null -w "200" 127.0.0.1:8000/ping)

if [ "$ping_status" -eq 200 ]
then
  echo "Restart successful"
else
  echo "Restart failed"
fi

# get the new count value
new_count_value=$(curl 127.0.0.1:8000/messages/count)

# testing persistence
if [ "$count_value" -eq "$new_count_value" ]
then
  echo "Persistence successful"
else
  echo "Persistence failed"
fi
