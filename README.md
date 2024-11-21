# Crawlab Python SDK

Python SDK for Crawlab

## Installation

```bash
pip install crawlab-sdk
```

## Usage

### CLI

```bash
crawlab-cli
```

### Scrapy Integration

In `settings.py`, add the following:

```python
ITEM_PIPELINES = {
    'crawlab.CrawlabPipeline': 300
}
```

## Development

### Install dependencies

```bash
pip install -r requirements.txt
```

### Compile gRPC

```bash
# Set the environment variable CRAWLAB_PROTO_PATH to the path of the gRPC proto files
export CRAWLAB_PROTO_PATH=/path/to/grpc/proto/files

# Compile gRPC to Python code
./compile_grpc.sh
```
