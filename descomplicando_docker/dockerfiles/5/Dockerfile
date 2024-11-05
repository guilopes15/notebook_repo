FROM golang:1.12.1 AS buildando

WORKDIR /app
ADD . .
RUN go build -o meugo

FROM alpine
WORKDIR /test
COPY --from=buildando /app/meugo /test/

ENTRYPOINT ./meugo
