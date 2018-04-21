class Entity(object):
    def __init__(self, typ, oid, version=None, action=None):
        self.typ = typ
        self.oid = oid
        self.version = version
        self.action = action
        self.members = []
        self.lat = None
        self.lon = None
        self.tags = {}
        if oid > 0:
            self.base = self.copy()
        else:
            self.base = None

    def copy(self):
        res = Entity(self.typ, self.oid, self.version, self.action)
        res.members = []
        for m in self.members:
            res.members.append(list(m))
        res.lat = self.lat
        res.lon = self.lon
        res.tags = dict(self.tags)
        return res

    def is_modified(self):
        if self.action or self.oid <= 0:
            return True
        if not self.base:
            return False
        if self.version > self.base.version:
            return True
        if self.tags != self.base.tags:
            return True
        if self.members != self.base.members:
            return True
        if self.lat != self.base.lat or self.lon != self.base.lon:
            return True
        return False

    def sort_key(self):
        if self.typ == 'node':
            g = 0
        elif self.typ == 'way':
            g = 1
        elif self.typ == 'relation':
            g = 2
        else:
            g = -1
        if self.action == 'delete':
            g = 22 - g
        elif self.action == 'modify':
            g = 10 + g
        return (g, self.oid)
