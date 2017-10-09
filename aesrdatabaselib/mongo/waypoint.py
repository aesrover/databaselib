from pymongo.collection import Collection

from typing import List

from ..base.waypoint import WaypointManager


class MongoWaypointManager(WaypointManager):
    wp_filter = {'type': 'AUTO_WP'}

    def __init__(self, wp_c: Collection):
        super().__init__()
        self.wp_c = wp_c

    def __wp_as_dict(self, raw_wp):
        return {
            'pos': tuple(raw_wp['pos']),
            'depth': raw_wp['depth'],
            'time': raw_wp['time']
        }

    def get_wps(self, lim: int = None) -> List[dict]:
        return [self.__wp_as_dict(e) for e in self.wp_c.find(self.wp_filter)]

    def _get_del_wp(self):
        wp = self.wp_c.find_one(self.wp_filter)
        if wp is not None:
            self.wp_c.delete_one(wp)
            wp = self.__wp_as_dict(wp)
        return wp

    def remove_wp(self, wp=None, pos=None, depth=None):
        if wp is None:
            filt = {}
            if pos is not None:
                filt['pos'] = pos

            if depth is not None:
                filt['depth'] = depth
        else:
            filt = wp

        self.wp_c.delete_many(filt)
