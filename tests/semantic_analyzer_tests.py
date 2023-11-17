import unittest
from src.lexer import Lexer
from src.parser import Parser
from src.semantic_analyzer import SemanticAnalyzer

class TestSemanticAnalyzer(unittest.TestCase):
   def setUp(self):
       self.lexer = Lexer("print('Hello, World!')")
       self.parser = Parser(self.lexer.tokenize())
       self.semantic_analyzer = SemanticAnalyzer(self.parser.parse())

   def test_analyze(self):
       self.semantic_analyzer.analyze()
       # This is a placeholder test. In a real semantic analyzer, you would check for semantic errors here.

if __name__ == '__main__':
   unittest.main()
