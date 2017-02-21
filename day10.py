class Bot(object):
    def __init__(self, low_to, high_to, low_type, high_type, bot_id):
        self.id = bot_id
        self.low_to = low_to
        self.high_to = high_to
        self.low_type = low_type
        self.high_type = high_type
        self.values = []

    def add_value(self, value):
        self.values.append(value)
        self.values = sorted(self.values)
        if self.values == [17, 61]:
            print self.id

    def __repr__(self):
        return 'Bot %d with low_to: %s, high_to %s and values %r' % (self.id, self.low_to, self.high_to, self.values)


def give(bot_id):
    bot = bots[bot_id]
    if len(bot.values) == 2:
        if bot.low_type == 'bot':
            bots[bot.low_to].add_value(bot.values[0])
            if len(bots[bot.low_to].values) == 2:
                give(bot.low_to)
        else:
            outputs[bot.low_to] = bot.values[0]
        if bot.high_type == 'bot':
            bots[bot.high_to].add_value(bot.values[1])
            if len(bots[bot.high_to].values) == 2:
                give(bot.high_to)
        else:
            outputs[bot.high_to] = bot.values[1]


with open('input_d10.txt') as f:
    lines = [line.strip('\n') for line in f.readlines()]

bots = {}
init_lines = []
outputs = {}

for line in lines:
    words = line.split()
    if words[0] == 'bot':
        bot_id = int(words[1])
        low_to = int(words[6])
        low_type = words[5]
        high_to = int(words[-1])
        high_type = words[-2]
        bots[bot_id] = Bot(low_to, high_to, low_type, high_type, bot_id)
    elif words[0] == 'value':
        init_lines.append(line)

for line in init_lines:
    words = line.split()
    bot = int(words[-1])
    value = int(words[1])
    bots[bot].add_value(value)

give(146)
