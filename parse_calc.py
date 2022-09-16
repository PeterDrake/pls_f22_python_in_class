tokens = []


def parse(token_stream):
    global tokens
    tokens = token_stream
    program()
    print("Parse successful")


def match(expected_type):
    global tokens
    if tokens[0][1] == expected_type:
        tokens = tokens[1:]  # Consume this token
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def program():
    if tokens[0][1] in ['id', 'read', 'write', '$$']:
        stmt_list()
        match('$$')
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def stmt_list():
    t = tokens[0][1]
    if t in ['id', 'read', 'write']:
        stmt()
        stmt_list()
    elif t == '$$':
        pass
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def stmt():
    t = tokens[0][1]
    if t == 'id':
        match('id')
        match(':=')
        expr()
    elif t == 'read':
        match('read')
        match('id')
    elif t == 'write':
        match('write')
        expr()
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def expr():
    t = tokens[0][1]
    if t in ['id', '(', 'number']:
        term()
        term_tail()
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def term_tail():
    t = tokens[0][1]
    if t in ['+', '-']:
        add_op()
        term()
        term_tail()
    elif t in [')', 'read', 'write', '$$']:
        pass
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def term():
    t = tokens[0][1]
    if t in ['id', 'number', '(']:
        factor()
        factor_tail()
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def factor_tail():
    t = tokens[0][1]
    if t in ['*', '/']:
        mult_op()
        factor()
        factor_tail()
    elif t in ['+', '-', ')', 'id', 'read', 'write', '$$']:
        pass
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def factor():
    t = tokens[0][1]
    if t == '(':
        match('(')
        expr()
        match(')')
    elif t == 'id':
        match('id')
    elif t == 'number':
        match('number')
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def add_op():
    t = tokens[0][1]
    if t == '+':
        match('+')
    elif t == '-':
        match('-')
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def mult_op():
    t = tokens[0][1]
    if t == '*':
        match('*')
    elif t == '/':
        match('/')
    else:
        raise SyntaxError("Parse error at " + str(tokens))
