def indent(lines, level=1):
    return ['  ' * level + line for line in lines]


def flatten(r):
    for i in r:
        if isinstance(i, list):
            for j in flatten(i):
                yield j
        else:
            yield i


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
        lines = list(flatten(statements))
        return '\n'.join(self.handle_indent(lines))

    def handle_indent(self, lines):
        i = 0
        indent = 0
        while i < len(lines):
            # move '{' to the end of previous line
            if lines[i] == '{' and i > 0:
                lines[i-1] += ' {'
                del(lines[i])
                indent += 1
                # and skip this line
                continue

            # merge "else if" lines
            if lines[i].startswith('if') and i > 0 and lines[i-1].endswith('else'):
                lines[i-1] += ' ' + lines[i]
                del(lines[i])
                continue

            # merge "} else" lines
            if lines[i].startswith('else') and i > 0 and lines[i-1].endswith('}'):
                lines[i-1] += ' ' + lines[i]
                del(lines[i])
                continue

            # insert empty line
            if not lines[i].startswith('}') and i > 0 and lines[i-1].endswith('}'):
                lines.insert(i, '')

            if lines[i] == '}':
                if indent > 0:
                    indent -= 1

            # add indent
            lines[i] = '  ' * indent + lines[i]

            # move to next line
            i += 1

        return lines

    def decompile_statement(self, ast):
        if 'if' in ast:
            result = [
                'if (%s)' % self.decompile_expr(ast['if']),
            ]

            result.append(self.decompile_block(ast['then']))

            if 'else' in ast:
                result.append('else')

                # don't add braces if the 'else' statement is another 'if'
                if not isinstance(ast['else'], list) and 'if' in ast['else']:
                    result.append(self.decompile_statement(ast['else']))
                else:
                    result.append(self.decompile_block(ast['else']))

            return result

        elif 'func' in ast:
            return self.decompile_action(ast)

    def decompile_block(self, ast):
        if isinstance(ast, list):
            statements = [self.decompile_statement(statement) for statement in ast]
        else:
            statements = [self.decompile_statement(ast)]

        return [
            '{',
            statements,
            '}',
        ]

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

        return [f'{func}({", ".join(params)})']

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
