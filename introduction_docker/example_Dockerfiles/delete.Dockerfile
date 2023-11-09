FROM alpine:3.18
RUN apk upgrade
RUN apk add wget curl python3 py3-pip
RUN apk del wget curl python3 py3-pip
