# Python Compiler

This is a simple Python compiler written in Python. It's designed to take Python source code and compile it into Python bytecode.

## Directory Structure

- `src/`: Contains the source code for the compiler. Each component of the compiler (lexer, parser, semantic analyzer, code generator, and optimizer) has its own Python file in this directory.

- `tests/`: Contains unit tests for each component of the compiler. Each test file corresponds to a component in the `src/` directory.

- `docs/`: Contains documentation for the project. Currently, this only includes this README file.

- `main.py`: The main entry point for the compiler. It imports and uses the components defined in the `src/` directory.

## How to Run

To run the compiler, you can use the following command:

```
bash python main.py
```

This will compile a simple source code string and print the optimized machine code.

## Testing

To run the unit tests, you can use the following command:

```
bash python -m unittest discover -s tests
```

This will run all the unit tests in the `tests/` directory and print the results.

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for an improvement, please open an issue. If you want to contribute code, please open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
