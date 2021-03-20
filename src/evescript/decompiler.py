def indent(lines, level=1):
    return ['  ' * level + line for line in lines]


def precedence(operator):
    if operator == '!':
        return 1
    elif operator == '&&':
        return 3
    elif operator == '||':
        return 4
    else:
        return 2


class EveScriptDecompiler:

    def decompile(self, ast):
        statements = [self.decompile_statement(statement) for statement in ast['statements']]
        return '\n\n'.join(statements)

    def decompile_statement(self, ast):
        expr = self.decompile_expr(ast['if'])
        actions = [self.decompile_action(action) for action in ast['then']]
        return '\n'.join([
            'if (%s) {' % expr,
            *indent(actions),
            '}'
        ])

    def decompile_expr(self, ast, prev_precedence=999):
        if isinstance(ast, dict):
            operator = self.decompile_operator(ast['operator'])
            current_precedence = precedence(operator)
            operands = [self.decompile_expr(operand, current_precedence) for operand in ast['operands']]

            use_parenthesis = current_precedence > prev_precedence

            if len(operands) == 1:
                if use_parenthesis:
                    return f'{operator}({operands[0]})'
                else:
                    return f'{operator}{operands[0]}'
            else:
                if use_parenthesis:
                    return f'({operands[0]} {operator} {operands[1]})'
                else:
                    return f'{operands[0]} {operator} {operands[1]}'
        else:
            return self.decompile_operand(ast)

    def decompile_operator(self, ast):
        return ast

    def decompile_action(self, ast):
        func = ast['func']
        params = [self.decompile_const(param) for param in ast['params']]

        return f'{func}({", ".join(params)})'

    def decompile_const(self, ast):
        if isinstance(ast, bool):
            if ast:
                return 'true'
            else:
                return 'false'
        elif isinstance(ast, str):
            return f'"{ast}"'
        else:
            return ast

    def decompile_operand(self, ast):
        if isinstance(ast, str) and ast.startswith('$'):
            return ast
        else:
            return self.decompile_const(ast)
