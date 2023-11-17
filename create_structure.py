import os

# Define the directories and files
directories = ['src', 'tests', 'docs']
files = ['lexer.py', 'parser.py', 'semantic_analyzer.py', 'code_generator.py', 'optimizer.py']
test_files = ['lexer_tests.py', 'parser_tests.py', 'semantic_analyzer_tests.py', 'code_generator_tests.py', 'optimizer_tests.py']

# Create the directories
for directory in directories:
   os.makedirs(directory, exist_ok=True)

# Create the files
for file in files:
   with open(f'src/{file}', 'w') as f:
       pass

for file in test_files:
   with open(f'tests/{file}', 'w') as f:
       pass

# Create the README file
with open('docs/README.md', 'w') as f:
   pass

# Create the main file
with open('main.py', 'w') as f:
   pass
