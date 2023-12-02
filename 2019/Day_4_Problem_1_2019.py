def is_increasing (number):
    for i in range(0,5):
        if int(number[i]) <= int(number[i+1]):
            continue
        else:
            return False
    return True

def has_adjacent_double (number):
    for i in range(0,5):
        if i == 0:
            if int(number[i]) == int(number[i+1]) and int(number[i+2]) > int(number[i]):
                return True
        elif i == 4:
            if int(number[i]) == int(number[i+1]) and int(number[i-1]) < int(number[i]):
                return True
        elif int(number[i]) == int(number[i+1]) and int(number[i+2]) > int(number[i]) and int(number[i-1]) < int(number[i]):
            return True
    return False
    
def check_range (number1, number2, result):
    for i in range(number1, number2):
        if is_increasing(str(i)) and has_adjacent_double(str(i)):
            print(i)
            result = result + 1    
    print(result)

#print(is_increasing("111011"))
#print(is_increasing("123456"))
#print(has_adjacent_double("111011"))
#print(has_adjacent_double("123456"))
#print(is_increasing("689998"))
#print(has_adjacent_double("689998"))
#print(has_adjacent_double("689999"))
#print(has_adjacent_double("688999"))
check_range(147981, 691423, 0)