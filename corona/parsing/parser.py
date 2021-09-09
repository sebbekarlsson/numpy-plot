from corona.parsing.lexer import Lexer
from corona.parsing.langtoken import TokenType
from corona.parsing.AST import ASTCompound, ASTBinop, ASTID


class Parser(object):


    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()


    def eat(self, token_type: TokenType):
        if self.current_token.type != token_type:
            print(f"Unexpected token {self.current_token.type}, was expecting {token_type}.")
            quit()

        self.current_token = self.lexer.get_next_token()
        return self.current_token

    def parse_id(self):
        value = self.current_token.value
        self.eat(TokenType.TOKEN_ID)
        return ASTID(value)

    def parse_factor(self):
        if self.current_token.type == TokenType.TOKEN_ID:
            return self.parse_id()


    def parse_term(self):
        return self.parse_factor()

    def parse_expr(self):
        left = self.parse_term()

        while self.current_token.type == TokenType.TOKEN_DOT:
            binop = ASTBinop(left, None, self.current_token)
            self.eat(self.current_token.type)
            binop.right = self.parse_term()
            left = binop

        while self.current_token.type in [
                TokenType.TOKEN_LT,
                TokenType.TOKEN_GT,
                TokenType.TOKEN_EQUALS_EQUALS,
                TokenType.TOKEN_NOT_EQUALS
        ]:
            binop = ASTBinop(left, None, self.current_token)
            self.eat(self.current_token.type)
            binop.right = self.parse_expr()
            left = binop
            return left

        return left

    def parse(self):
        return self.parse_compound()

    def parse_compound(self):
        children = []

        while self.current_token.type != TokenType.TOKEN_EOF:
            children.append(self.parse_expr())

        return ASTCompound(children)
