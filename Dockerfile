FROM python:3.7-alpine

RUN apk add git bash && pip install git+https://github.com/kazk1018/trello-kpt

ENTRYPOINT ["trello"]
