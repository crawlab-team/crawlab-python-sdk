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

### Save Scraped Items
    
```python
from crawlab import save_item

scraped_items = [
    {
        'name': 'item1',
        'value': 'value1'
    },
    {
        'name': 'item2',
        'value': 'value2'
    }
]

for item in scraped_items:
    save_item(item) 
```

## Development

### Pre-requisites

```bash
pip install poetry
```

### Install dependencies

```bash
poetry install
```
