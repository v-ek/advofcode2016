import hashlib

puzzle_input = 'abbhdwsy'
pw_length = 0
ctnr = 0 
pwd_chars = []
pwd_chars_p2 = [None] * 8
while pw_length < 8 or None in pwd_chars_p2:
    to_hash = puzzle_input + str(ctnr)
    hexdigest = hashlib.md5(to_hash).hexdigest()
    if hexdigest[:5] == '00000':
        if pw_length < 8:
            pwd_chars.append(hexdigest[5])
            pw_length += 1
        try:
            pos = int(hexdigest[5])
            if pos < 8 and pwd_chars_p2[pos] is None:
                pwd_chars_p2[pos] = hexdigest[6]
        except Exception, e:
            pass    
    ctnr += 1

password = ''.join(pwd_chars)
password_p2 = ''.join(pwd_chars_p2)


print password
print password_p2