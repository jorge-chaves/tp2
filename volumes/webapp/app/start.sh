#!/bin/bash

pip install -r /app/requirements.txt
python /app/app.py &

wait -n
exit $?
