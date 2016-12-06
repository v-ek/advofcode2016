from collections import Counter

with open('input_d6.txt') as f: 
    lines = [line.strip('\n') for line in f.readlines()]

# Transpose the input
columns = zip(*lines)

message_list = []
message_list_p2 = []

for column in columns:
    ctnr = Counter(column)
    most_common = ctnr.most_common(1)[0][0]
    least_common = ctnr.most_common()[-1][0]
    message_list.append(most_common)
    message_list_p2.append(least_common)

message = ''.join(message_list)
message_2 = ''.join(message_list_p2)

print message
print message_2