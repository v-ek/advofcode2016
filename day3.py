def l1_norm(v1):
    """Simple l1_norm calculation of any list-like"""
    norm = 0
    for coord in v1:
        norm += abs(coord)
    return norm

def is_triangle(v1):
    """ checks if a sorted list-like of length 3 is a triangle"""
    sides = list(v1)
    sides.sort()
    if l1_norm(sides[:2]) > sides[2]:
        return True
    return False


def split_int(line):
    """ strips, splits and returns the line as a list of ints"""
    line_out = line.strip().split()
    line_out = [int(part) for part in line_out]
    return line_out

with open('input_d3.txt') as f: 
    lines = [line.strip('\n') for line in f.readlines()]

# part 1
num_correct = 0
for line in lines:
    sides = line.strip().split()
    sides = [int(side) for side in sides]
    sides.sort()
    if l1_norm(sides[:2]) > sides[2]:
        num_correct += 1

print num_correct

# part 2
lines_clean = [split_int(line) for line in lines]
columns = zip(*lines_clean)
length = len(columns[0])

num_correct_2 = 0
for column in columns:
    for ii in range(0,length,3):
        coords = column[ii:ii+3]
        print coords
        if is_triangle(coords):
            num_correct_2 += 1

print num_correct_2            