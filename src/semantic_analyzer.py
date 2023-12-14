class SemanticAnalyzer:
    def __init__(self, parse_tree):
        self.parse_tree = parse_tree

    def analyze(self):
        for node in self.parse_tree:
            if node["type"] == "PRINT":
                for value in node["values"]:
                    assert type(value) == str, "Values must be strings."