final_states = [1, 4, 6]

transitions = [{'.': 5},
               {'e': 2, 'E': 2, '.': 6},
               {'+': 3, '-': 3},
               {},
               {},
               {},
               {'e': 2, 'E': 2}]

for d in '0123456789':
    transitions[0][d] = 1
    transitions[1][d] = 1
    transitions[2][d] = 4
    transitions[3][d] = 4
    transitions[4][d] = 4
    transitions[5][d] = 6
    transitions[6][d] = 6

for c in ' \t\n':
    transitions[0][c] = 0


def scan(program):
    tokens = []
    current_token = ''
    state = 0
    for c in program + '\n':
        if c in transitions[state]:
            current_token += c
            state = transitions[state][c]
        elif state in final_states:
            tokens += [current_token]
            current_token = c
            state = transitions[0][c]
        else:
            print('ERROR: ' + current_token + c)
            return tokens
        if state == 0:
            current_token = ''
    if state in final_states:
        tokens += [current_token]
    return tokens


with open('test1.numbers') as f:
    print(scan(f.read()))
