# Edge Cloud Aggregator

## Setup Virtual environment

```bash
python3 -m venv venv
```

## Build Docker Container

```bash
docker build -t dev.local/fed-edge-model-selector:0.1 .
docker run dev.local/fed-edge-model-selector <BROKER_ADDRESS>
```
