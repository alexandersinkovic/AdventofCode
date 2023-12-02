f = open("Day7_input.txt", "r")

currrent_path = ''

for line in f:
    command = line.split(' ')
    if (command[0] == '$'):
        if (command[1] == 'ls'):
            continue
        currrent_path = currrent_path

        continue
    if (command[0] == 'dir'):

        continue
