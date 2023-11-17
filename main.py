from src.lexer import Lexer
from src.parser import Parser
from src.semantic_analyzer import SemanticAnalyzer
from src.code_generator import CodeGenerator
from src.optimizer import Optimizer

def main():
   # Create a new Lexer
   lexer = Lexer("print('Hello, World!')")

   # Tokenize the source code
   tokens = lexer.tokenize()

   # Create a new Parser
   parser = Parser(tokens)

   # Parse the tokens into a parse tree
   parse_tree = parser.parse()

   # Create a new SemanticAnalyzer
   semantic_analyzer = SemanticAnalyzer(parse_tree)

   # Analyze the parse tree for semantic errors
   semantic_analyzer.analyze()

   # Create a new CodeGenerator
   code_generator = CodeGenerator(parse_tree)

   # Generate machine code from the parse tree
   machine_code = code_generator.generate_code()

   # Create a new Optimizer
   optimizer = Optimizer(machine_code)

   # Optimize the machine code
   optimized_machine_code = optimizer.optimize()

   # Print the optimized machine code
   print(optimized_machine_code)

if __name__ == "__main__":
   main()
