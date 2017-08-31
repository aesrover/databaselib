from typing import List


class DataHandler:
    """
    Used for making sub-classes to store data read by the `Store` class.

    Override:
        - `store`: store a single `dict` of transducer data.
        - `store_multiple`: store multiple `dict`s of transducer data. Defaults to running `store` for each element.
    """
    def store_one(self, data: dict):
        """ Store a single `dict` of transducer data. """
        raise NotImplementedError("`store` not implemented in sub-handler: {}".format(self))

    def store_many(self, data: List[dict]):
        """ Store multiple `dict`s of transducer data. Defaults to running `store` for each element. """
        for d in data:
            self.store_one(d)
