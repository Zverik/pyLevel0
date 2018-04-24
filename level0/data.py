try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree


class Entity(object):
    def __init__(self, typ, oid):
        self.type = typ
        self.id = oid
        self.version = None
        self.action = None
        self.members = []
        self.lat = None
        self.lon = None
        self.tags = {}
        self.conflict = None

    @staticmethod
    def from_xml(el, action=None):
        e = Entity(el.tag, int(el.get('id')))
        v = el.get('version', None)
        if v:
            e.version = int(v)
        e.action = action or el.get('action', None)
        for tag in el.findall('tag'):
            e.tags[tag.get('k')] = tag.get('v')
        if e.type == 'node':
            e.lat = float(el.get('lat'))
            e.lon = float(el.get('lon'))
        elif e.type == 'way':
            for nd in el.findall('nd'):
                e.members.append(int(nd.get('ref')))
        elif e.type == 'relation':
            for m in el.findall('member'):
                e.members.append((m.get('type'), int(m.get('ref')), m.get('role', '')))
        return e

    def to_xml(self, osc=False):
        el = etree.Element(self.type, id=str(self.id))
        if self.version:
            el.set('version', str(self.version))
        if self.action and not osc:
            el.set('action', self.action)
        if self.type == 'node':
            el.set('lat', str(self.lat))
            el.set('lon', str(self.lon))
        elif self.type == 'way':
            for nd in self.members:
                etree.SubElement(el, 'nd', ref=str(nd))
        elif self.type == 'relation':
            for m in self.members:
                etree.SubElement(el, 'member', type=m[0], ref=str(m[1]), role=m[2] or '')
        for k, v in self.tags.items():
            etree.SubElement(el, 'tag', k=k, v=v)
        return el

    def copy(self):
        res = Entity(self.type, self.id, self.version, self.action)
        res.members = []
        for m in self.members:
            res.members.append(list(m))
        res.lat = self.lat
        res.lon = self.lon
        res.tags = dict(self.tags)
        return res

    def is_modified(self, base):
        if self.action or self.id <= 0:
            return True
        if not base:
            return False
        if self.version > base.version:
            return True
        if self.tags != base.tags:
            return True
        if self.members != base.members:
            return True
        if self.lat != base.lat or self.lon != base.lon:
            return True
        return False

    def sort_key(self):
        if self.type == 'node':
            g = 0
        elif self.type == 'way':
            g = 1
        elif self.type == 'relation':
            g = 2
        else:
            g = -1
        if self.action == 'delete':
            g = 22 - g
        elif self.action == 'modify':
            g = 10 + g
        return (g, self.id)

    def __lt__(self, other):
        return self.sort_key() < other.sort_key()

    def __eq__(self, other):
        # TODO: multiple created objects???
        return self.sort_key() == other.sort_key()
