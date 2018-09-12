#!/bin/bash
if [ -f bot.pid ]; then
        kill -9 `cat bot.pid`
        rm bot.pid
fi
if [ -f logs/log.txt ]; then
        fmt="$(date)"
        fmt="$(date +'%d-%m')"
        mv "logs/log.txt" "logs/$fmt-log.txt"
fi
nohup python3 -u ./main.py > logs/log.txt 2>&1 &
echo $! > bot.pid
