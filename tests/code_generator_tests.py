import unittest
from src.lexer import Lexer
from src.parser import Parser
from src.semantic_analyzer import SemanticAnalyzer
from src.code_generator import CodeGenerator

class TestCodeGenerator(unittest.TestCase):
   def setUp(self):
       self.lexer = Lexer("print('Hello, World!')")
       self.parser = Parser(self.lexer.tokenize())
       self.semantic_analyzer = SemanticAnalyzer(self.parser.parse())
       self.code_generator = CodeGenerator(self.semantic_analyzer.analyze())

   def test_generate_code(self):
       code = self.code_generator.generate_code()
       # This is a placeholder test. In a real code generator, you would check that the generated code is correct here.

if __name__ == '__main__':
   unittest.main()
