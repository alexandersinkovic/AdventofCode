from aoc_fetcher import get_data

input = get_data(2022, 13)

pairs = []
input = input.splitlines()

for i in range(0, len(input), 3):
    pairs.append((input[i], input[i+1]))

print(pairs[0])

class Packet:
    children = []

    def __init__(self, children):
        print('Begin', children)
        if (not (children == '')):
            i = 0
            while (i < len(children)):
                print('Current Index: ', i)
                if ( children[i] == ','):
                    i += 1
                    continue
                elif (children[i] == '['):
                    left_bracket = i
                    counter = 1
                    while (not (counter == 0)):
                        i += 1
                        if (children[i] == '['):
                            counter += 1
                        if (children[i] == ']'):
                            counter -= 1
                    #print('Case "["', children[left_bracket+1:i])
                    newPacket = Packet(children[left_bracket+1:i])
                    print(self.children)
                    self.children.append(newPacket)
                else:
                    left_bracket = i
                    while (not ( i == len(children)) and children[i].isnumeric() ):
                        i += 1
                    print('Case Number', children[left_bracket:i])
                    print(self.children)
                    self.children.append(int(children[left_bracket:i]))
                i += 1

test = Packet('[1,[2],3]')
print(test)
print(test.children)

def packetComparator(p1, p2):
    pass
