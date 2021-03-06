from corona.parsing.lexer import Lexer
from corona.parsing.langtoken import TokenType
from corona.parsing.parser import Parser
from corona.parsing.emit import emit


def create_filter(query: str, db):
    lexer = Lexer(query)
    parser = Parser(lexer)
    ast = parser.parse()

    return emit(ast, db, db.classmap)
