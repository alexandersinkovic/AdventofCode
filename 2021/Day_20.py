from aoc_fetcher import get_data

input = get_data(2021, 20)
#input = open("Day_20_testInput.txt").read()

def part1():
    data = input. strip().split("\n\n")
    decode = data[0]
    res_image = data[1].splitlines()
    #print(res_image)
    padding = '.'
    map_padding = {
        '.': '0',
        '#': '1'
    }
    #apply padding
    for _ in range(50):
        apply_padding = '.' if padding == '.' else '#'
        #print("apply_padding:", apply_padding, padding)
        image = [apply_padding + line + apply_padding for line in res_image]
        extend = ''.join([apply_padding] * len(image[0]))
        padded_image = [extend]
        for line in image:
            padded_image.append(line)
        padded_image.append(extend)
        #print("Padded Image: ", padded_image)
        res_image = []
        for y in range(len(padded_image)):
            res_pixels = ''
            for x in range(len(padded_image[0])):
                pixels = ''
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x+j < 0 or x+j >= len(padded_image[0]) or y+i < 0 or y+i >= len(padded_image):
                            pixels += padding
                        else:
                            pixels += padded_image[y+i][x+j]
                pixels = ''.join([map_padding[c] for c in pixels])
                #print(pixels)
                res_pixels += decode[int(pixels, 2)]
                #print(res_pixels)
            res_image.append(res_pixels)
        #print("Res Image")
        #for lin in res_image:
        #    print(lin)
        padding = '#' if padding == '.' else '.'
    count = 0
    for line in res_image:
        for c in line:
            if c == '#':
                count += 1
    #print(res_image)
    print(count)
part1()
