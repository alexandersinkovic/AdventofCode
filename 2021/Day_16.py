from aoc_fetcher import get_data
import math

input = get_data(2021, 16)
#input = "8A004A801A8002F478"
#input = "620080001611562C8802118E34"
#input = "C0015000016115A2E0802F182340"
#input = "A0016C880162017C3686B18A3D4780"
#input = "C200B40A82"
#input = "04005AC33890"
#input = "880086C3E88112"
#input = "CE00C43D881120"
#input = "D8005AC2A8F0"
#input = "F600BC2D8F"
#input = "9C005AC2F8F0"
#input = "9C0141080250320F1802104A08"
switch_dict = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1]
}

def parse_literal_value(data, i):
    #print(i)
    #print("while")
    literal = ""
    while(data[i] != "0"):
        #print("while", i)
        literal += data[i+1: i+5]
        i += 5
    literal += data[i+1: i+5]
    i += 5

    return i, int(literal, 2)

def call_sub_packets(data, i):
    values = []
    if data[i] == "0":
        i += 1
        length_of_sub_packets = int(data[i: i+15], 2)
        i += 15
        end_of_sub_packets = i + length_of_sub_packets
        while(i < end_of_sub_packets):
            #print(i)
            i, val = parse_operator_packet(data, i)
            values.append(val)
    else:
        #print("found 1")
        i += 1
        length_of_sub_packets = int(data[i: i+11], 2)
        i += 11
        #print("length_of_sub_packets", length_of_sub_packets)
        for _ in range(length_of_sub_packets):
            #print(i)
            i, val = parse_operator_packet(data, i)
            values.append(val)
    return i, values

def parse_operator_packet(data, i):
    #print(i)
    #print(data[i:i+6])
    #print(sum_of_packet_versions)
    #sum_of_packet_versions += increase_sum_of_packet_versions(data, i)
    #print(sum_of_packet_versions)
    i += 3
    if int(data[i: i+3], 2) == 4:
        #print("found literal")
        i += 3
        return parse_literal_value(data, i)
    #print(i)
    #print(type(i))
    type_id = int(data[i: i+3], 2)
    i, sub_packets = call_sub_packets(data, i+3)
    return i, switch_dict[type_id](sub_packets)


def increase_sum_of_packet_versions(data, i):
    return int(data[i: i+3], 2)

def part1():
    data = [f"{int(x, 16):0>4b}" for x in input.strip()]
    #print(data[-2:])
    data = ''.join(data)
    #data = data.rstrip("0")
    #print(data)

    i = 0
    #print(len(data))
    #print(data)
    #while(i < len(data)):
        #print("Before", i)
    i, result = parse_operator_packet(data, i)
        #print("after", i)
    print(result)

part1()
#print(int("101", 2))
#print(int("A", 16))
#print(f"{4:0>4b}")
