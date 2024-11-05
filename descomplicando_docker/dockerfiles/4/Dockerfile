FROM golang:1.12.1

WORKDIR /app
ADD . .
RUN go build -o meugo
ENTRYPOINT ./meugo
