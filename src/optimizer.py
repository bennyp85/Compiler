class Optimizer:
    def __init__(self, machine_code):
        self.machine_code = machine_code

    def optimize(self):
        lines = self.machine_code.split("\n")
        new_lines = []
        for line in lines:
            if not line.startswith("OUT"):
                new_lines.append(line)
                continue
            value = line.strip().split()[1]
            if value[-1] == ";":
                value = value[:-1]
            new_lines.append(f"OUT {value};")
        return "\n".join(new_lines)