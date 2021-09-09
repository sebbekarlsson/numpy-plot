from corona.parsing.AST import AST, ASTCompound, ASTID, ASTBinop
from corona.parsing.langtoken import TokenType
from corona.models.case import Case
from corona.db import DB

# cases.date == vaccines.date


# Rack upp handen nar er kod ser ut sa har
class QueryInfo(object):

    def __init__(self, row, field, operator, query_info):
        self.row = row
        self.field = field
        self.operator = operator
        self.query_info = query_info


def emit(ast: AST, db:DB):
    if isinstance(ast, ASTCompound):
        return emit_ast_compound(ast, db)

    if isinstance(ast, ASTID):
        return emit_ast_ast_id(ast, db)

    if isinstance(ast, ASTBinop):
        return emit_ast_binop(ast, db)


    print("Dont know how to emit: ", ast)
    quit()


def emit_ast_compound(ast: ASTCompound, db:DB):
    infos = []

    for child in ast.children:
        return emit(child, db)
        # infos.append(emit(child, db))

    return infos

def emit_ast_ast_id(ast: ASTID, db:DB):
    return ast.value


# Rack upp handen nar ni har detta
def emit_ast_binop(ast: ASTBinop, db:DB):
    if ast.token.type != TokenType.TOKEN_DOT:
        left = emit(ast.left, db)
        operator = ast.token.type
        right = emit(ast.right, db)

        model_a_name = left[0]
        model_a_data = list(left[1])
        model_a_field = left[2]

        model_b_name = right[0]
        model_b_data = list(right[1])
        model_b_field = right[2]


        if operator == TokenType.TOKEN_EQUALS_EQUALS:
            return filter(lambda x: x[1][model_a_field] == model_b_data[x[0]][model_b_field], enumerate(model_a_data))
    else:
       left = emit(ast.left, db)
       rows = db.get(left, Case)
       field = emit(ast.right, db)

       return (left, rows, field)
