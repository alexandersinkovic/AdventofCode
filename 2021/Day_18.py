from aoc_fetcher import get_data
import math

input = get_data(2021, 18)
#input = ['[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]']
#input = open('Day_18_testInput.txt').read()
#input = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'


def addition(sn):
    while(True):
        #print()
        #print(sn)
        count_brackets = 0
        need_explode = False
        need_split = True
        explode_idx = 0
        for idx, c in enumerate(sn):
            if count_brackets >= 5:
                need_explode = True
                explode_idx = idx
                #print(explode_idx)
                #print(sn[explode_idx])
                break
            if c == '[':
                count_brackets += 1
            elif c == ']':
                count_brackets -= 1
        explode_left_double_digit = 2 if sn[explode_idx+1].isnumeric() else 1
        #print(sn[explode_idx+1+explode_left_double_digit])
        explode_right_double_digit = 2 if sn[explode_idx+2+explode_left_double_digit].isnumeric() else 1
        #print(sn[explode_idx])
        #print(explode_idx)
        #print(sn)
        #print()
        if need_explode:
            for left in range(explode_idx-1, 0, -1):
                #print(sn[left].isnumeric(), sn[left-1].isnumeric())
                if sn[left].isnumeric() and not sn[left-1].isnumeric():
                    prev_len = len(sn)
                    sn = sn[:left] + str(int(sn[left]) + int(sn[explode_idx: explode_idx + explode_left_double_digit])) + sn[left+1:]
                    if not len(sn) == prev_len:
                        explode_idx += explode_left_double_digit
                    break
                elif sn[left].isnumeric() and sn[left-1].isnumeric():
                    prev_len = len(sn)
                    sn = sn[:left-1] + str(int(sn[left-1 : left+1]) + int(sn[explode_idx: explode_idx + explode_left_double_digit])) + sn[left+1:]
                    if not len(sn) == prev_len:
                        explode_idx += explode_left_double_digit
                    break
            #print("check right side")
            for right in range(explode_idx + 5, len(sn)-1):
                #print(sn[right].isnumeric(), sn[right+1].isnumeric())
                if sn[right].isnumeric() and not sn[right+1].isnumeric():
                    #print()
                    #print(sn)
                    #print(right, explode_idx)
                    #print(sn[right])
                    #print(sn[explode_idx])
                    #print(sn[explode_idx + 2])
                    sn = sn[:right] + str(int(sn[right]) + int(sn[explode_idx + 2: explode_idx + 2 + explode_right_double_digit])) + sn[right+1:]
                    break
                elif sn[right].isnumeric() and sn[right+1].isnumeric():
                    sn = sn[:right] + str(int(sn[right: right+2]) + int(sn[explode_idx + 2: explode_idx + 2 + explode_right_double_digit])) + sn[right+2:]
                    break
            sn = sn[:explode_idx-explode_left_double_digit] + '0' + sn[explode_idx + 3 + explode_right_double_digit:]
        else:
            need_split = False
            for idx, c in enumerate(sn):
                if c.isnumeric() and sn[idx+1].isnumeric():
                    need_split = True
                    val = int(c + sn[idx+1])
                    insert = f'[{int(val/2)},{math.ceil(val/2)}]'
                    sn = sn[:idx] + insert + sn[idx+2:]
                    break
        #print(need_split)
        if not need_split:
            break
    return sn


def magnitude_calculator(sn):
    #print(sn)
    if len(sn) == 1:
        return int(sn)
    elif sn[1] == '[':
        count = 1
        for idx, c in enumerate(sn[2:-1]):
            #print(count)
            if c == '[':
                count += 1
            elif c == ']':
                count -= 1
            if count == 0:
                #print(sn[1:idx+3])
                return 3 * magnitude_calculator(sn[1:idx+3]) + 2 * magnitude_calculator(sn[idx+4:-1])
    else:
        return 3 * int(sn[1]) + 2 * magnitude_calculator(sn[3: -1])

def part1():
    #data = input
    data = input.strip().splitlines()
    res = data[0]
    for line in data[1:]:
        print(f'[{res},{line}]')
        res = addition(f'[{res},{line}]')
    print(magnitude_calculator(res))

def part2():
    data = input.strip().splitlines()
    max_magnitude = 0
    for x in range(0,len(data)):
        for y in range(x, len(data)):
            cur_mag = magnitude_calculator(addition(f'[{data[x]},{data[y]}]'))
            if cur_mag > max_magnitude:
                max_magnitude = cur_mag
    print(max_magnitude)
part2()
#print(magnitude_calculator(input))
