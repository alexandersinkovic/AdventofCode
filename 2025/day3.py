from aocd import get_data

DATA = get_data(day=3, year=2025)

INPUT = DATA.splitlines()
#INPUT = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']

def clear_from_idx(nums, idx):
    for i in range(idx, len(nums)):
        nums[i] = 0

def insert_jolt(my_num, n, start_from):
    for i in range(start_from,len(my_num)):
        if my_num[i] < n:
            my_num[i] = n
            clear_from_idx(my_num, i+1)
            return

def p1():
    res = 0
    for line in INPUT:
        highest = 0
        second_highest = 0
        nums = [int(c) for c in line]
        for n in nums[:-1]:
            if n > highest:
                highest = n
                second_highest = 0
            elif n == highest:
                second_highest = n
            else:
                if n > second_highest:
                    second_highest = n
        if nums[-1] > second_highest:
            second_highest = nums[-1]
        res += (highest*10) + second_highest
    print(res)

def p2():
    res = 0
    for line in INPUT:
        my_num = [0]*12
        nums = [int(c) for c in line]
        for idx, n in enumerate(nums):
            remaining = 0
            if len(nums) - idx - 1 < 12:
                remaining = 12 - (len(nums) - idx)
            insert_jolt(my_num, n, remaining)
        res += int(''.join(str(c) for c in my_num))
    print(res)

p2()