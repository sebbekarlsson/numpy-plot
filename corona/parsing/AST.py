from enum import Enum

from corona.parsing.token import Token


class ASTType(Enum):
    AST_BINOP = 0              # cases.date,  5 + 5
    AST_ID = 1
    AST_STRING = 2
    AST_NUMBER =  3


class AST(object):
    pass


class ASTBinop(AST):

    def __init__(self, left: AST, right: AST, token: Token):
        self.left = left
        self.right = right
        self.token = token


class ASTID(AST):

    def __init__(self, value: str):
        self.value = value
