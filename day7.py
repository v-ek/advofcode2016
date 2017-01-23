import re

def is_abba(string):
    abba_re = r'(\w)(\w)\2\1'
    matches = re.findall(abba_re, string)
    for match in matches:
        #print matches
        if match[0] != match[1]:
            return True
    return False

def is_aba(string):
    return string[0] == string[2] and string [1] != string[0] and string.isalpha()

def supports_ssl(string1, string2):
    abas_1 = []
    abas_2 = []
    for ii in range(0, len(string1)-2):
        substring = string1[ii:ii+3]
        if is_aba(substring):
            abas_1.append(substring)
    
    for ii in range(0, len(string2)-2):
        substring = string2[ii:ii+3]
        if is_aba(substring):
            abas_2.append(substring)
    for aba in abas_1:
        bab = aba[1] + aba[0] + aba[1]
        if bab in abas_2:
            return True
    return False



with open('input_d7.txt') as f: 
    lines = [line.strip('\n') for line in f.readlines()]


hypernet_re = r'\[\w+\]'

num_supporting_tls = 0
num_supporting_ssl = 0

for line in lines:
    text_outside_hn = re.sub(hypernet_re, ' ', line)
    text_hn = re.findall(hypernet_re, line)
    text_hn = ''.join(text_hn)

    if is_abba(text_outside_hn) and not is_abba(text_hn):
        num_supporting_tls += 1
    
    if supports_ssl(text_outside_hn, text_hn):
        num_supporting_ssl += 1
print num_supporting_tls
print num_supporting_ssl
