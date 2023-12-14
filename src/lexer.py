class Lexer:
    WORDS = {"print": "KEYWORD"}

    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.reading_word = False
        self.current_word = ""

    def tokenize(self):
        tokens = []
        while self.position < len(self.source_code):
            char = self.source_code[self.position]
            if char.isspace():
                self.position += 1
                continue
            elif char == "'":
                self._handle_string()
            elif char == "(":
                tokens.append({"type": "LEFT_PAREN", "value": "("})
                self.position += 1
            elif char == ")":
                tokens.append({"type": "RIGHT_PAREN", "value": ")"})
                self.position += 1
            else:
                if self.reading_word:
                    self.current_word += char
                else:
                    self.reading_word = True
                    self.current_word = char
                if self.position + 1 >= len(self.source_code) or not self.source_code[self.position+1].isalnum():
                    word_type = None
                    if self.current_word in self.WORDS:
                        word_type = self.WORDS[self.current_word]
                    token = {"type": word_type, "value": self.current_word} if word_type else {"type": "IDENTIFIER", "value": self.current_word}
                    tokens.append(token)
                    self.reading_word = False
                    self.current_word = ""
            self.position += 1
        return tokens
    
    def _handle_string(self):
        self.position += 1
        string = ""
        while self.position < len(self.source_code) and self.source_code[self.position] != "'":
            string += self.source_code[self.position]
            self.position += 1
        if self.position >= len(self.source_code):
            raise Exception("Unmatched quote found.")
        tokens = [{"type": "STRING", "value": string}]
        self.position += 1
        return tokens