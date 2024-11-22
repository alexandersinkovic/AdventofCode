#from aoc_fetcher import get_data
import math

f = open("Day_14_in.txt", "r")
f1 = open("Day_14_test1.txt", "r")
f2 = open("Day_14_test2.txt", "r")
f3 = open("Day_14_test3.txt", "r")
f4 = open("Day_14_test4.txt", "r")
f5 = open("Day_14_test5.txt", "r")

input = f.read().split('\n')

#print(input)

def part1(req_dict, dist_in):
    #req_dict = create_req_dict(input)
    dist = dist_in
    left_over = {}
    ore = 0
    #print(list(dist.keys()))
    while len(list(dist.keys())) > 0:
        k = list(dist.keys())[0]
        v = dist.pop(k)
        #print(k, v)
        #print('use leftover')
        if k in left_over:
            if v < left_over[k]:
                add_to_dict(k, -v, left_over)
                continue
            elif v == left_over[k]:
                left_over.pop(k)
            else:
                v = v - left_over[k]
                left_over.pop(k)
        #print(k, v)
        convertion = req_dict[k]
        needed_amount = 1
        if v > convertion[0]:
            needed_amount = math.ceil(v / convertion[0])
        for x, y in convertion[1]:
            if x == 'ORE':
                ore += y * needed_amount
            else:
                add_to_dict(x, y*needed_amount, dist)
        #print(convertion[0], needed_amount, v)
        if convertion[0] * needed_amount - v > 0:
            add_to_dict(k, convertion[0] * needed_amount - v, left_over)
        #print(dist.items())
        #print(left_over.items())
    #print('ORE:', ore)
    return ore

#number_of_fuel per manuellem Ausprobieren bestimmt
def part2(input):
    req_dict = create_req_dict(input)
    number_of_fuel = 1935265
    dist = {'FUEL': number_of_fuel}
    print(1000000000000)
    return part1(req_dict, dist)



def add_to_dict(k, v, dict):
    if k in dict:
        dict[k] += v
    else:
        dict[k] = v


def create_req_dict(input: [str]):
    dict = {}
    for rule in input:
        cost, out = rule.split(' => ')
        cost_parts = cost.split(', ')
        cost_lst = [[c_key, int(c_amount)] for c_amount, c_key in [c.split(' ') for c in cost_parts]]
        out_amount, out_key = out.split(' ')
        dict[out_key] = [int(out_amount), cost_lst]
    return dict


def ggT(a, b):
    # Die Funktion ggT berechnet den größten gemeinsamen Teiler zweier Zahlen a und b.
    # Die Zwischenergebnisse und das Endergebnis der Funktion ggT werden in einer Variable gespeichert. Dafür wird die Variable resultat deklariert.
    # Im Fall, dass die erste Zahl a gleich 0 ist, ist das Ergebnis gleich b (der zweiten Zahl). Im Fall, dass a jedoch ungleich 0 ist, wird die ggT Funktion mit den geänderten beziehungsweise angepassten Argumenten ggT(b MOD a, a).
    if a == 0:
        resultat = b
    else:
        resultat = ggT(b % a, a)

    return resultat

def kgV(a, b):
    # Die Funktion kgV soll das kleinste gemeinsame Vielfach zweier Zahlen a und b berechnen. Die zwei Zahlen wurden als Argument an die kgV Funktion übergeben.
    # Um das Ergebnis zu speichern, wird in einer Variable gespeichert. Dafür wird die Variable resultat deklariert.
    # Um das kgV zu berechnen werden die zwei Zahlen a und b zuerst multipliziert und das Ergebnis wird dann durch den größten gemeinsamen Teiler der zwei Zahlen a und b geteilt. Das Ergebnis wird in der Variablen resultat gespeichert.
    resultat = float(a * b) / ggT(a, b)

    return resultat

#part1(create_req_dict(input), {'FUEL': 82892753 })
print(part2(input))