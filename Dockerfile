FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY app/go.mod app/go.sum ./
RUN go mod download
COPY app/ .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app .
EXPOSE 8090
CMD ["./app"]
