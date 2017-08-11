FROM node:8.1.2

# Prepare the environment
RUN apt-get update && \
    apt-get install -y build-essential python && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app

WORKDIR /app

COPY . /app/

ENV PORT=3000
EXPOSE $PORT

CMD python -m SimpleHTTPServer $PORT
