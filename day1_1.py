
def parse_instr(instr, state):
    # Parse instruction of form [A-Z][0-9]+
    # Left (pos) N V S E
    # Right N E S V
    
    _directions = ('N', 'V', 'S', 'E')
    _num_dirs = len(_directions)
    turn = instr[0]
    steps = int(instr[1:])
    dir_index = _directions.index(state['facing'])
    
    if turn == 'L':
        state['facing'] = _directions[(dir_index + 1) % _num_dirs]
    elif turn == 'R':
        state['facing'] = _directions[(dir_index - 1) % _num_dirs]

    direction = state['facing']
    pos = state['pos']
    #state['prior_locs'].add(tuple(pos))
    # Old implementation
    # walk(pos, state['facing'], steps)
    # Ugly brute force solution with storing all prior positions
    for ii in range(0,steps):
        if direction == 'N':
            pos[1] = pos[1] + 1
        elif direction == 'S':
            pos[1] = pos[1] - 1
        elif direction == 'V':
            pos[0] = pos[0] - 1
        elif direction == 'E':
            pos[0] = pos[0] + 1
        state['prior_locs'].append(tuple(pos))

def walk(pos, direction, steps):
    """ Walk, changes coordinates in-place """
    if direction == 'N':
        pos[1] = pos[1] + steps
    elif direction == 'S':
        pos[1] = pos[1] - steps
    elif direction == 'V':
        pos[0] = pos[0] - steps
    elif direction == 'E':
        pos[0] = pos[0] + steps

def l1_norm(v1):
    """Simple l1_norm calculation of any list-like"""
    norm = 0
    for coord in v1:
        norm += abs(coord)
    return norm

def get_duplicates(list_):
    seen = []
    seen2 = []
    for item in list_:
        if item in seen:
            seen2.append(item)
        else:
            seen.append(item)
    return seen2

def create_instr_from_file(fname='input_d1.txt'):
    with open('input_d1.txt') as f: 
        lines = [x.strip('\n') for x in f.readlines()]

    instructions = []
    for line in lines:
        x = line.split(',')

    for instr in x:
        instructions.append(instr.strip())
    return instructions


state = {
    'facing' : 'N', 
    'pos': [0, 0],
    'prior_locs' : [],
}

instructions = create_instr_from_file()

for instr in instructions:
    parse_instr(instr, state)

print '1: ', l1_norm(state['pos'])
print '2: ', l1_norm(get_duplicates(state['prior_locs'])[0])