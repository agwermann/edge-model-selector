# Edge Cloud Aggregator

## Setup Virtual environment

```bash
python3 -m venv venv
```

## Build Docker Container

```bash
docker build -t fed-edge-controller:0.1 .
docker run edge-controller <BROKER_ADDRESS>
```
