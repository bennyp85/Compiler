import unittest
from src.lexer import Lexer
from src.parser import Parser

class TestParser(unittest.TestCase):
   def setUp(self):
       self.lexer = Lexer("print('Hello, World!')")
       self.parser = Parser(self.lexer.tokenize())

   def test_parse(self):
       parse_tree = self.parser.parse()
       self.assertEqual(len(parse_tree), 1)
       self.assertEqual(parse_tree[0].type, 'PRINT_STATEMENT')
       self.assertEqual(parse_tree[0].children[0].type, 'STRING')
       self.assertEqual(parse_tree[0].children[0].value, "'Hello, World!'")

if __name__ == '__main__':
   unittest.main()
