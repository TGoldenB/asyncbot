#!/bin/bash
# just a script to start the bot without killing it, use this if you do not have permission to kill
#!/bin/bash
if [ -f logs/log.txt ]; then
        fmt="$(date)"
        fmt="$(date +'%d-%m')"
        mv "logs/log.txt" "logs/$fmt-log.txt"
fi
nohup python3 -u ./main.py > logs/log.txt 2>&1 &
rm bot.pid
echo $! > bot.pid
chown $USER:sarpadmins bot.pid
chown $USER:sarpadmins "logs/$fmt-log.txt"
chmod 770 bot.pid
chmod 770 "logs/$fmt-log.txt"
