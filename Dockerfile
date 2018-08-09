FROM python:3.5-alpine
RUN apk add --no-cache build-base libffi-dev opus ffmpeg
RUN python3 -m pip install -U discord.py
RUN apk del build-base
ENTRYPOINT [ "/usr/local/bin/python", "-u", "main.py" ]
