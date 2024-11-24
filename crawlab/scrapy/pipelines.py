from crawlab import save_item


class CrawlabPipeline(object):
    """Pipeline for saving scraped items to Crawlab's database."""

    def process_item(self, item, spider):
        # Save the result to Crawlab's database
        save_item(item)

        # Return the item for potential further processing by other pipelines
        return item
