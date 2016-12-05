from collections import Counter
import re

def get_code_and_decrypt(line):
    """Check if a line is a real room and returns code for real rooms and
    zero otherwise"""

    # Regex
    letters_re = r'[a-z\-]+(?=[0-9]+)'
    numbers_re = r'(?<=\w|\-)[0-9]+'
    checksum_re = r'(?<=\[)[a-z]+'

    # Get the parts
    letters = re.match(letters_re, line).group(0)
    letters_cln = letters.replace('-', '')
    cntr = Counter(letters_cln)
    common = cntr.most_common()
    common.sort(key=lambda x:(-x[1], x[0]))
    
    top_5_list = [item[0] for item in common][:5]
    top_5 = ''.join(top_5_list)
    code = re.search(numbers_re, line).group(0)
    checksum = re.search(checksum_re, line).group(0)
    
    if checksum == top_5:
        code =  int(code)
    else:
        code = 0

    if code != 0:
        decrypted = decrypt(letters, code)
    else:
        decrypted = None
    return code, decrypted

def decrypt(text, code):
    """decrypt a line"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    length = len(alphabet)
    decrypted = []
    for letter in text:
        if letter == '-':
            decrypted.append(' ')
        else:
            index = alphabet.index(letter)
            new_index = (index + code) % length
            decrypted.append(alphabet[new_index])
    return ''.join(decrypted)

def get_room_code(line):
    code, _ = get_code_and_decrypt(line)
    return code

with open('input_d4.txt') as f: 
    lines = [line.strip('\n') for line in f.readlines()]

sum_of_codes = 0

for line in lines:
    # sum_of_codes += get_room_code(line)
    code, decrypted = get_code_and_decrypt(line)
    sum_of_codes += code
    if decrypted:
        if 'north' in decrypted:
            print decrypted, code
print sum_of_codes