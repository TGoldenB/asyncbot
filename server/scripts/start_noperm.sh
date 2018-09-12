#!/bin/bash
# just a script to start the bot without killing it, use this if you do not have permission to kill
python3 terminate.py
if [ -f logs/log.txt ]; then
        fmt="$(date)"
        fmt="$(date +'%d-%m')"
        mv "logs/log.txt" "logs/$fmt-log.txt"
fi
nohup python3 -u ./main.py > logs/log.txt 2>&1 &
echo $! > bot.pid
