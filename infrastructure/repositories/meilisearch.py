
from dotenv import load_dotenv
import os
import meilisearch

class Meilisearch:
    def __init__(self):
        load_dotenv()
        _api_key = str(os.getenv("MEILISEARCH_API_KEY"))
        _base_url = f'https://{str(os.getenv("MEILISEARCH_INSTANCE"))}.meilisearch.io'
        _index = str(os.getenv("MEILISEARCH_INDEX"))
        _client = meilisearch.Client(_base_url, _api_key)
        self.index = _client.index(_index)

    def write(self, data):
        self.index.add_documents([data])

    def search(self, field):
        return self.index.search(field)['hits']
    
    def reset_index(self):
        self.index.delete_all_documents()