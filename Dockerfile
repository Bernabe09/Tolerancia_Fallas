FROM alpine:3.10

RUN apk add  --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /bot_telegram

COPY . /bot_telegram/

CMD ["python3", "src/bot_telegram"]