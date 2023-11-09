FROM alpine:3.18
RUN apk upgrade; \
    apk add wget curl python3 py3-pip; \
    apk del wget curl python3 py3-pip; \
