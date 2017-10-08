from pymongo.collection import Collection

from typing import List, Tuple

from ..base.waypoint import WaypointManager


class MongoWaypointManager(WaypointManager):
    wp_filter = {'type': 'AUTO_WP'}

    def __init__(self, wp_c: Collection):
        super().__init__()
        self.wp_c = wp_c

    def get_wps(self, lim: int = None) -> List[Tuple[float, float, float]]:
        return [e['pos'] for e in self.wp_c.find(self.wp_filter)]

    def _get_del_wp(self):
        wp = self.wp_c.find_one(self.wp_filter)
        if wp is not None:
            self.wp_c.delete_one(wp)
            wp = (*wp['pos'], wp['depth'])
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

        self.wp_c.delete_one(filt)
