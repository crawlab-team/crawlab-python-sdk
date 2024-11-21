from crawlab import save_item
from crawlab.config import get_task_id
from crawlab.entity.result import Result


class CrawlabPipeline(object):
    """Pipeline for saving scraped items to Crawlab's database."""

    def process_item(self, item, spider):
        # Get the task ID from the current crawling task
        task_id = get_task_id()
        
        # Skip processing if no task ID is available
        if not task_id:
            return item

        # Convert the scraped item to a Crawlab Result object
        result = Result(item)
        
        # Associate the result with the current task
        result.set_task_id(task_id)
        
        # Save the result to Crawlab's database
        save_item(result)

        # Return the item for potential further processing by other pipelines
        return item
