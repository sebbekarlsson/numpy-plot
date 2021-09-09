from corona.parsing.AST import AST, ASTCompound, ASTID, ASTBinop
from corona.parsing.langtoken import TokenType
from corona.db import DB

# cases.date == vaccines.date


# Rack upp handen nar er kod ser ut sa har
class QueryInfo(object):

    def __init__(self, row, field, operator, query_info):
        self.row = row
        self.field = field
        self.operator = operator
        self.query_info = query_info


def emit(ast: AST, db:DB, classmap):
    if isinstance(ast, ASTCompound):
        return emit_ast_compound(ast, db, classmap)

    if isinstance(ast, ASTID):
        return emit_ast_ast_id(ast, db, classmap)

    if isinstance(ast, ASTBinop):
        return emit_ast_binop(ast, db, classmap)


    print("Dont know how to emit: ", ast)
    quit()


def emit_ast_compound(ast: ASTCompound, db:DB, classmap):
    for child in ast.children:
        return emit(child, db, classmap)

def emit_ast_ast_id(ast: ASTID, db:DB, classmap):
    return ast.value

def emit_ast_binop(ast: ASTBinop, db:DB, classmap):
    if ast.token.type != TokenType.TOKEN_DOT:
        left = emit(ast.left, db, classmap)
        operator = ast.token.type
        right = emit(ast.right, db, classmap)

        model_a_name = left[0]
        model_a_data = list(left[1])
        model_a_field = left[2]

        model_b_name = right[0]
        model_b_data = list(right[1])
        model_b_field = right[2]


        if operator == TokenType.TOKEN_EQUALS_EQUALS:
            result1 = list(map(lambda tup: tup[1], filter(
                lambda x: x[1].__getattribute__(model_a_field) == model_b_data[x[0]].__getattribute__(model_b_field),
                enumerate(model_a_data)
            )))


            return map(lambda x: {**x.__dict__, "children": list(filter(lambda y: (
               y.__getattribute__(model_b_field) == x.__getattribute__(model_b_field)
            ), model_b_data))} , result1)

    else:
       left = emit(ast.left, db, classmap)
       clazz = classmap.get(left)

       if not clazz:
           raise Exception(f"Could not map {left} to a class")

       rows = db.get(left, clazz)
       field = emit(ast.right, db, classmap)

       return (left, rows, field)
