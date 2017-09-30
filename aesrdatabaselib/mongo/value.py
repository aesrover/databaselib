from pymongo.collection import Collection

from ..base.value import GetPositionValue


class MongoGetPositionValue(GetPositionValue):
    def __init__(self, col: Collection, match: dict, lim: int, pos_key: str):
        self.col = col
        self.match = match
        self.lim = lim
        self.pos_key = pos_key

    def _find(self, lim, sort=1):
        res = self.col.find(self.match).sort({'_id': sort})
        for l in range(lim):
            yield res[l]

    def get_early(self, lim=1):
        return self._find(lim, -1)

    def get_recent(self, lim=1):
        return self._find(lim, 1)

    def get_early_pos(self, avg=1):
        for doc in self.get_early(self.lim):
            yield doc[self.pos_key]

    def get_recent_pos(self, avg=1):
        for doc in self.get_recent(self.lim):
            yield doc[self.pos_key]
