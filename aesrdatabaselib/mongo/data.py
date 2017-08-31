from pymongo.collection import Collection
from typing import List

from ..base.data import DataHandler


class MongoDataHandler(DataHandler):
    def __init__(self, col: Collection):
        self.col = col

    def store_one(self, data: dict):
        self.col.insert_one(dict)

    def store_many(self, data: List[dict]):
        self.col.insert_many(data)
