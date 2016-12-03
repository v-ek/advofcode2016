def walk_square(pos, direction):
    """ Walk on grid, changes coordinates in-place """
    """ Made for the first part of day 2 """
    if direction == 'U':
        if pos[1] < 2:
            pos[1] += 1
    elif direction == 'D':
        if pos[1] > 0:
            pos[1] -= 1
    elif direction == 'L':
        if pos[0] > 0:
            pos[0] -= 1
    elif direction == 'R':
        if pos[0] < 2:
            pos[0] += 1

def walk_grid(pos, direction):
    """ walk on the grid with the middle being (0,0) """
    # observe that out of bound is if l1_norm > 2
    if direction == 'U':
        pos[1] += 1
        if l1_norm(pos) > 2:
            pos[1] -= 1
    elif direction == 'D':
        pos[1] -= 1
        if l1_norm(pos) > 2:
            pos[1] += 1
    elif direction == 'L':
        pos[0] -= 1
        if l1_norm(pos) > 2:
            pos[0] += 1
    elif direction == 'R':
        pos[0] += 1
        if l1_norm(pos) > 2:
            pos[0] -= 1

    


def l1_norm(v1):
    """Simple l1_norm calculation of any list-like"""
    norm = 0
    for coord in v1:
        norm += abs(coord)
    return norm

with open('input_d2.txt') as f: 
    lines = [x.strip('\n') for x in f.readlines()]

# dict for transaling pos to key value
pos_to_var_1 = {
    (0, 0): 7,
    (0, 1): 4,
    (0, 2): 1,
    (1, 0): 8,
    (1, 1): 5,
    (1, 2): 2,
    (2, 0): 9,
    (2, 1): 6,
    (2, 2): 3,
}

pos_to_var_2 = {
    (0, 2): 1,
    (-1, 1): 2,
    (0, 1): 3,
    (1, 1): 4,
    (-2, 0): 5,
    (-1, 0): 6,
    (0, 0): 7,
    (1, 0): 8,
    (2, 0): 9,
    (-1, -1): 'A',
    (0, -1): 'B',
    (1, -1): 'C',
    (0,-2): 'D',
}

pos_1 = [1,1]
pos_2 = [-2,0]
end_pos_1 = []
end_pos_2 = []

for line in lines:
    for letter in line:
        walk_square(pos_1, letter)
        walk_grid(pos_2, letter)
    end_pos_1.append(tuple(pos_1))
    end_pos_2.append(tuple(pos_2))

code_1 = [pos_to_var_1[pos] for pos in end_pos_1]
code_2 = [pos_to_var_2[pos] for pos in end_pos_2]
print code_1, code_2