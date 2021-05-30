CO2-Server
===

## Overview
A WebSocket server that sends data acquired from the [CO2-mini](https://www.kk-custom.co.jp/emp/CO2-mini.html).
It sends data periodically while it is connected.

## How to build and run

```bash
docker-compose build
```

```bash
docker-compose up -d
```

## Environment variables
- WS_HOST: WebSocket host
- WS_PORT: WebSocket port
- INTERVAL: Interval to acquire data
