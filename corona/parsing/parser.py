from corona.parsing.lexer import Lexer
from corona.parsing.token import TokenType


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
