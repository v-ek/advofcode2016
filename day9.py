
def decompress(line):
    chars = []
    pos = 0
    length = len(line)

    while pos < length:
        curr_char = line[pos]

        if curr_char == '(':
            pos += 1
            num_chars_str = ''
            repeat_times_str = ''

            while line[pos] != 'x':
                num_chars_str += line[pos]
                pos += 1

            pos += 1
            num_chars = int(num_chars_str)

            while line[pos] != ')':
                repeat_times_str += line[pos]
                pos += 1
            pos +=1
            repeat_times = int(repeat_times_str)
            chars.extend([line[pos:pos + num_chars]] * repeat_times)
            pos += num_chars

        else:
            chars.append(curr_char)
            pos += 1

    return ''.join(chars)


with open('input_d9.txt') as f:
    lines = [line.strip('\n') for line in f.readlines()]
full_input = ''.join(lines)
print len(decompress(full_input))
