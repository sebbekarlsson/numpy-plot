from corona.parsing.lexer import Lexer
from corona.parsing.langtoken import TokenType


query = "cases.date == vaccines.date"


lexer = Lexer(query)

token = lexer.get_next_token()

while token.type != TokenType.TOKEN_EOF:
    print(token.value)
    token = lexer.get_next_token()
