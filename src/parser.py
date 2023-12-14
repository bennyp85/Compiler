class Parser:
    KEYWORDS = ["print"]

    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        ast = []
        while self.index < len(self.tokens):
            token = self.tokens[self.index]
            if token["type"] == "KEYWORD":
                if token["value"] == "print":
                    ast.append(self._parse_print())
            self.index += 1
        return ast
    
    def _parse_print(self):
        token = self.tokens[self.index]
        self.index += 1
        assert token["type"] == "KEYWORD" and token["value"] == "print", "Expected 'print'"
        values = []
        while self.index < len(self.tokens) and self.tokens[self.index]["type"] != "RIGHT_PAREN":
            token = self.tokens[self.index]
            if token["type"] == "STRING":
                values.append(token["value"])
            self.index += 1
        return {"type": "PRINT", "values": values}