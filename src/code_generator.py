class CodeGenerator:
    def __init__(self, parse_tree):
        self.parse_tree = parse_tree

    def generate_code(self):
        machine_code = ""
        for node in self.parse_tree:
            if isinstance(node, dict):
                if node["type"] == "PRINT":
                    machine_code += self._generate_print_code(node)
        return machine_code
    
    def _generate_print_code(self, node):
        return f"OUT {node['value']}\n"