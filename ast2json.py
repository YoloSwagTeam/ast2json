# Copyright (c) 2013, Laurent Peuch <cortex@worlddomination.be>
# Copyright (c) 2015, Eddy Ernesto del Valle Pino <xigmatron@gmail.com>
#
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of the University of California, Berkeley nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json

from _ast import AST
from ast import parse


class AstJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, AST):
            value = {
                attr: getattr(obj, attr)
                for attr in dir(obj)
                if not attr.startswith('_')
            }
            value['node_type'] = obj.__class__.__name__
            return value
        return super(AstJsonEncoder, self) .default(obj)


def ast2json(node, *args, **kwargs):
    return AstJsonEncoder(*args, **kwargs).encode(node)


def ast2dict(node):
    result = {}
    result['node_type'] = node.__class__.__name__.lower()
    for attr in dir(node):
        if not attr.startswith("_") and attr not in ('lineno', 'col_offset'):
            value = getattr(node, attr)
            if isinstance(value, AST):
                value = ast2dict(value)
            elif isinstance(value, list):
                value = [ast2dict(n) for n in value]
            result[attr] = value
    return result


class Tag:

    def __init__(self, name=None, attrs=None, children=None):
        self.name = (name or attrs.pop('node_type', '')).lower()
        self.attrs = {}

        self.children = [Tag(attrs=child) for child in children or []]

        for attr, value in (attrs or {}).items():
            if isinstance(value, list):
                self.children.append(Tag(name=attr, children=value))
            elif isinstance(value, dict):
                self.children.append(Tag(name=attr, children=[value]))
            else:
                self.attrs[attr] = value

    def __str__(self):
        attrs = []

        for attr, value in self.attrs.items():
            attrs.append('%(attr)s="%(value)s"' % locals())

        attrs = ' '.join(attrs)

        head = '%(name)s %(attrs)s' % {'name': self.name, 'attrs': attrs}
        return '<%(head)s>\n%(children)s</%(name)s>' % {
            'name': self.name,
            'head': head.strip(),
            'children': '\n'.join(str(node) for node in self.children) + '\n'
        }


def ast2xml(node):
    return Tag(attrs=ast2dict(node))


if __name__ == '__main__':
    import yaml
    import sys
    print(yaml.dump(ast2dict(parse(open(sys.argv[1]).read()))))
    print(ast2xml(parse(open(sys.argv[1]).read())))
