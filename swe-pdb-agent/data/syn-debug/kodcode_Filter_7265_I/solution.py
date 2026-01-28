class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token('NUMBER', result)

    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.number()
            if self.current_char == '+':
                self.advance()
                return Token('ADD', '+')
            if self.current_char == '-':
                self.advance()
                return Token('SUB', '-')
            if self.current_char == '*':
                self.advance()
                return Token('MUL', '*')
            if self.current_char == '/':
                self.advance()
                return Token('DIV', '/')
            if self.current_char == '(':
                return Token('LPAREN', '(')
            if self.current_char == ')':
                return Token('RPAREN', ')')
            raise Exception(f"Invalid character: {self.current_char}")
        return Token('EOF', None)

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message):
        raise Exception(message)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Unexpected token: {self.current_token.type}, expected: {token_type}")

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return token
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        else:
            self.error(f"Unexpected token in FACTOR: {token.type}")

    def term(self):
        node = self.factor()
        while self.current_token.type in ('MUL', 'DIV'):
            token = self.current_token
            if token.type == 'MUL':
                self.eat('MUL')
            elif token.type == 'DIV':
                self.eat('DIV')
            node = (token, node, self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in ('ADD', 'SUB'):
            token = self.current_token
            if token.type == 'ADD':
                self.eat('ADD')
            elif token.type == 'SUB':
                self.eat('SUB')
            node = (token, node, self.term())
        return node

    def parse(self):
        return self.expr()