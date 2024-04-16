#!/bin/bash
data="$(curl http://worldtimeapi.org/api/timezone/Asia/Kolkata | jq '.datetime')"
echo ${data//\"/}
date -s ${data//\"/}
