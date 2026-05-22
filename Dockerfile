FROM ubuntu:latest
LABEL authors="emre"

ENTRYPOINT ["top", "-b"]