from corona.parsing.lexer import Lexer
from corona.parsing.langtoken import TokenType
from corona.parsing.parser import Parser


query = "cases.date == vaccines.date"


lexer = Lexer(query)
parser = Parser(lexer)
ast = parser.parse()

print(ast)
