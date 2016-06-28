import ast
import json
import unittest

import ast2json


class TestApi(unittest.TestCase):
    def test_run(self):
        with open('./test/samples/one_function.py', 'rt') as f:
            j = ast2json.ast2json(ast.parse(f.read()))

        self.assertTrue(j)
        self.assertIn('body', j)
        self.assertEqual(j, json.loads(json.dumps(j)))
