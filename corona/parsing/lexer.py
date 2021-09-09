from corona.parsing.langtoken import Token, TokenType
import string


class Lexer(object):

    def __init__(self, src):
        self.src = src + " "
        self.length = len(src)
        self.index = 0

    def char(self):
        return self.src[min(self.length, self.index)]

    def advance(self):
       if self.index < self.length:
           self.index += 1
           return True
       return False

    def skip_whitespace(self):
        while self.char() in [" ", "\t", "\n", "\r"]:
            self.advance()

    def parse_id(self):
        buff = ""
        while self.char().isalnum() and self.index < self.length:
            buff += self.char()
            self.advance()


        return Token(TokenType.TOKEN_ID, buff)


    def peak(self):
        return self.src[min(self.length - 1, self.index + 1)]

    def get_next_token(self):
       while self.index < self.length - 1:
           self.skip_whitespace()

           if self.char().isalnum():
               token = self.parse_id()
               return token


           if self.char() == ".":
               token = Token(TokenType.TOKEN_DOT, self.char())
               self.advance()
               return token

           if self.char() == "=":
               if self.peak() == "=":
                   token = Token(TokenType.TOKEN_EQUALS_EQUALS, "==")
                   self.advance()
                   self.advance()
                   return token
           if self.char() == "!":
               if self.peak() == "=":
                   token = Token(TokenType.TOKEN_NOT_EQUALS, "!=")
                   self.advance()
                   self.advance()
                   return token
           if self.char() == "<":
               token = Token(TokenType.TOKEN_LT, self.char())
               self.advance()
               return token
           if self.char() == ">":
               token = Token(TokenType.TOKEN_GT, self.char())
               self.advance()
               return token


       return Token(TokenType.TOKEN_EOF, None)
