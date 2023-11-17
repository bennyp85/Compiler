import unittest
from src.lexer import Lexer

class TestLexer(unittest.TestCase):
   def setUp(self):
       self.lexer = Lexer("print('Hello, World!')")

   def test_tokenize(self):
       tokens = self.lexer.tokenize()
       self.assertEqual(len(tokens), 4)
       self.assertEqual(tokens[0].type, 'KEYWORD')
       self.assertEqual(tokens[0].value, 'print')
       self.assertEqual(tokens[1].type, 'OPEN_PARENTHESIS')
       self.assertEqual(tokens[1].value, '(')
       self.assertEqual(tokens[2].type, 'STRING')
       self.assertEqual(tokens[2].value, "'Hello, World!'")
       self.assertEqual(tokens[3].type, 'CLOSE_PARENTHESIS')
       self.assertEqual(tokens[3].value, ')')

if __name__ == '__main__':
   unittest.main()
