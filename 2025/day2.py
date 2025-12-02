from aocd import get_data

DATA = get_data(day=2, year=2025)
INPUT = [x.split('-') for x in DATA.split(',')]

def is_even_length(s):
    return len(s) % 2 == 0

def get_lowest_even_length(s):
    return int('1' + '0' * len(s))

res = 0

for lower, upper in INPUT:
    lower_num = int(lower)
    upper_num = int(upper)
    print(lower_num, upper_num)

    if not is_even_length(lower):
        lower_num = get_lowest_even_length(lower)
        lower = str(lower_num)
        if lower_num > upper_num:
            continue

    print(lower_num, upper_num)
    
    lower_half = lower[:len(lower)//2]
    upper_half = upper[:-len(lower)//2]


    while int(lower_half) <= int(upper_half):
        candidate = lower_half + lower_half
        candidate_num = int(candidate)
        if candidate_num >= lower_num and candidate_num <= upper_num:
            res += candidate_num
        lower_half = str(int(lower_half) + 1)

print(res)