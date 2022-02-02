FROM python:3.8-alpine

WORKDIR /http

RUN adduser -u 1111 -H -S -D httpUser

USER httpUser

COPY http_server.py test.html ./

ENV MY_HTTP_PORT=8080

EXPOSE $MY_HTTP_PORT

CMD [ "python3",  "http_server.py" ]