from corona.parsing.lexer import Lexer
from corona.parsing.langtoken import TokenType
from corona.parsing.AST import ASTCompound


class Parser(object):


    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()


    def eat(self, token_type: TokenType):
        self.current_token = self.lexer.get_next_token()
        if self.current_token.type != token_type:
            print(f"Unexpected token {self.current_token.type}, was expecting {token_type}.")
            quit()

        return self.current_token

    def parse_id(self):
        value = self.current_token.value
        self.eat(TOKEN_ID)
        return ASTID(value)

    def parse_factor(self):
        if self.current_token.type == TOKEN_ID:
            return self.parse_id()

    def parse_expr(self):
        left = self.parse_factor()

        while self.current_token.type in [
                TOKEN_LT,
                TOKEN_GT,
                TOKEN_DOT,
                TOKEN_EQUALS_EQUALS,
                TOKEN_NOT_EQUALS
        ]:
            binop = ASTBinop(left, self.parse_expr(), self.current_token)
            self.eat(self.current_token.type)
            left = binop

        return left

    def parse(self):
        expr = self.parse_expr()
        return expr

    def parse_compound(self):
        children = []

        while self.current_token.type != TOKEN_EOF:
            children.append(self.parse())

        return ASTCompound(children)
