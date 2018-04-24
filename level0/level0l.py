from data import Entity


def userdata_cmp(e):
    if e.type == 'node':
        grade = 0 if e.tags else 4
    elif e.type == 'way':
        grade = 1
    elif e.type == 'relation':
        grade = 2
    else:
        grade = -1
    return (grade, e.id)


def to_l0l(data, fileobj):
    def short_type(t):
        if t[0] == 'n':
            return 'nd'
        elif t[0] == 'w':
            return 'wy'
        return 'rel'

    need_nl = False
    tmp_id = 0
    for e in sorted(data, key=userdata_cmp):
        tmp_id += 1
        if need_nl or e.type != 'node':
            fileobj.write('\n')
        need_nl = e.type != 'node' or e.tags or e.conflict

        # TODO: conflict

        if e.action == 'delete':
            fileobj.write('-')
        fileobj.write(e.type)
        if e.id != 0:
            fileobj.write(' {}'.format(e.id))
        if e.type == 'node' and e.lat and e.lon:
            fileobj.write(': {}, {}'.format(e.lat, e.lon))
        fileobj.write('\n')
        for k, v in e.tags.items():
            fileobj.write('  {} = {}\n'.format(k.replace('=', '\\='), v))
        if e.type == 'way':
            for nd in e.members:
                fileobj.write('  nd {}\n'.format(nd))
        elif e.type == 'relation':
            for m in e.members:
                fileobj.write('  {} {}{}\n',
                              short_type(m[0]),
                              m[1],
                              '' if not m[2] else ' ' + m[2])


def from_l0l(fileobj, base):
    data = []
    line_no = 0
    for line in fileobj:
        line_no += 1
        # TODO
    return sorted(data)
