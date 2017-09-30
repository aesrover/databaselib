class GetDatabaseValue:
    def get_recent(self, lim=1):
        raise NotImplementedError

    def get_early(self, lim=1):
        raise NotImplementedError


class GetPositionValue(GetDatabaseValue):
    def get_recent_pos(self, avg=1):
        raise NotImplementedError

    def get_early_pos(self, avg=1):
        raise NotImplementedError
