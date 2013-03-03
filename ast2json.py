from ast import parse


def parse_module(module):
    return [recursive_call(x) for x in module.body]


def parse_tree(tree):
    return recursive_call(tree)


def parse_import(import_node):
    return {
        '_type': 'Import',
        'col_offset': import_node.col_offset,
        'lineno': import_node.lineno,
        'names': [recursive_call(x) for x in import_node.names],
    }


def parse_alias(alias):
    return {
        '_type': 'alias',
        'asname': alias.asname,
        'name': alias.name,
    }


def parse_import_from(import_from):
    return {
        '_type': 'ImportFrom',
        'col_offset': import_from.col_offset,
        'level': import_from.level,
        'lineno': import_from.lineno,
        'module': import_from.module,
        'names': [recursive_call(x) for x in import_from.names],
    }


function_mapping = {
    'Module': parse_module,
    'Import': parse_import,
    'alias': parse_alias,
    'ImportFrom': parse_import_from,
}


def unknow_node(node):
    print node, [node.__class__.__name__]
    from IPython import embed
    embed()
    import sys
    sys.exit(0)


def recursive_call(node):
    return function_mapping.get(node.__class__.__name__, unknow_node)(node)


if __name__ == '__main__':
    from pprint import pprint
    pprint(parse_tree(parse(open("vodka.py", "r").read())))
