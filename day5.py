import hashlib

puzzle_input = 'abbhdwsy'
pw_length = 0
ctnr = 0 
# List for the first part
pwd_chars = []
# List for the second part
pwd_chars_p2 = [None] * 8

# Brute force in a loop
while pw_length < 8 or None in pwd_chars_p2:
    to_hash = puzzle_input + str(ctnr)
    hexdigest = hashlib.md5(to_hash).hexdigest()
    if hexdigest[:5] == '00000':
        if pw_length < 8:
            pwd_chars.append(hexdigest[5])
            pw_length += 1

        # Se if pos is int, else pass
        try:
            pos = int(hexdigest[5])
            if pos < 8 and pwd_chars_p2[pos] is None:
                pwd_chars_p2[pos] = hexdigest[6]
        except ValueError:
            pass    
    ctnr += 1

password = ''.join(pwd_chars)
password_p2 = ''.join(pwd_chars_p2)


print password
print password_p2