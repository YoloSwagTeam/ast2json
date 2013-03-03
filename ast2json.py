from _ast import AST
from ast import parse


def ast_to_json(node):
    to_return = {}
    to_return['_type'] = node.__class__.__name__
    for attr in dir(node):
        if attr.startswith("_"):
            continue
        to_return[attr] = get_value(getattr(node, attr))

    return to_return


def get_value(attr_value):
    if attr_value is None:
        return attr_value
    if isinstance(attr_value, (int, basestring)):
        return attr_value
    if isinstance(attr_value, list):
        return [ast_to_json(x) for x in attr_value]
    if isinstance(attr_value, AST):
        return ast_to_json(attr_value)
    print attr_value


if __name__ == '__main__':
    import json
    print json.dumps(ast_to_json(parse(open(__file__, "r").read())), indent=4)
