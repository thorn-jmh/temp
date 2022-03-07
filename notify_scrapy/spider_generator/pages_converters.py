pages_converters = {}


def pages_converter(func):
    pages_converters[func.__name__] = func
    return func


def get_pages_converter(name: str, default=None):
    return pages_converters.get(name, default)


@pages_converter
def list_dot_htm(pages: dict):
    count = 0
    res = []

    def traverse(item, columns):
        nonlocal count
        k, v = item
        if type(v) is str:
            res.append({
                'name': 'page%d' % count,
                'initial_url': v,
                'page_url': v.rstrip('list.htm') + 'list%d.htm',
                'column': columns + [k]
            })
            count += 1
            return
        for sub_item in v.items():
            traverse(sub_item, columns + [k])

    for item in pages.items():
        traverse(item, [])

    return res


@pages_converter
def list_dot_psp(pages: dict):
    count = 0
    res = []

    def traverse(item, columns):
        nonlocal count
        k, v = item
        if type(v) is str:
            res.append({
                'name': 'page%d' % count,
                'initial_url': v,
                'page_url': v.rstrip('list.psp') + 'list%d.psp',
                'column': columns + [k]
            })
            count += 1
            return
        for sub_item in v.items():
            traverse(sub_item, columns + [k])

    for item in pages.items():
        traverse(item, [])

    return res


@pages_converter
def and_page_equals(pages: dict):
    count = 0
    res = []

    def traverse(item, columns):
        nonlocal count
        k, v = item
        if type(v) is str:
            res.append({
                'name': 'page%d' % count,
                'initial_url': v,
                'page_url': v + '&page=%d',
                'column': columns + [k]
            })
            count += 1
            return
        for sub_item in v.items():
            traverse(sub_item, columns + [k])

    for item in pages.items():
        traverse(item, [])

    return res


@pages_converter
def slash_p(pages: dict):
    count = 0
    res = []

    def traverse(item, columns):
        nonlocal count
        k, v = item
        if type(v) is str:
            res.append({
                'name': 'page%d' % count,
                'initial_url': v,
                'page_url': v + '/p/%d',
                'column': columns + [k]
            })
            count += 1
            return
        for sub_item in v.items():
            traverse(sub_item, columns + [k])

    for item in pages.items():
        traverse(item, [])

    return res


@pages_converter
def and_p_equals(pages: dict):
    count = 0
    res = []

    def traverse(item, columns):
        nonlocal count
        k, v = item
        if type(v) is str:
            res.append({
                'name': 'page%d' % count,
                'initial_url': v,
                'page_url': v + '&p=%d',
                'column': columns + [k]
            })
            count += 1
            return
        for sub_item in v.items():
            traverse(sub_item, columns + [k])

    for item in pages.items():
        traverse(item, [])

    return res
