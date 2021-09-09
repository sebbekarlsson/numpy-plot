from enum import Enum


class TokenType(Enum):
    TOKEN_ID = 0
    TOKEN_DOT = 1
    TOKEN_EQUALS_EQUALS = 2
    TOKEN_NOT_EQUALS = 3
    TOKEN_LT = 4
    TOKEN_GT = 5
    TOKEN_EOF = 6


class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value
