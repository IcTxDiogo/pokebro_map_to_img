import os
import numpy as np
from PIL import Image

TAM = 256
TAMBLOCK = 8
TAMZMIN = 0
TAMZMAX = 16
RGB = 3
BLOCKSIZE = 65536


def check_color(hex_number):
    if hex_number == "0c":
        return [0, 102, 0]
    if hex_number == "18":
        return [0, 204, 0]
    if hex_number == "1b":
        return [0, 204, 153]
    if hex_number == "1e":
        return [0, 255, 0]
    if hex_number == "28":
        return [51, 0, 204]
    if hex_number == "29":
        return [51, 0, 255]
    if hex_number == "33":
        return [51, 102, 153]
    if hex_number == "4d":
        return [51, 0, 255]
    if hex_number == "56":
        return [102, 102, 102]
    if hex_number == "72":
        return [153, 51, 0]
    if hex_number == "79":
        return [153, 102, 51]
    if hex_number == "81":
        return [153, 153, 153]
    if hex_number == "ac":
        return [204, 204, 204]
    if hex_number == "b3":
        return [204, 255, 255]
    if hex_number == "ba":
        return [255, 51, 0]
    if hex_number == "c0":
        return [255, 102, 0]
    if hex_number == "cf":
        return [255, 204, 153]
    if hex_number == "d2":
        return [255, 255, 0]
    if hex_number == "d7":
        return [255, 255, 255]
    return [0, 0, 0]


array_color_unique = []

for z in range(TAMZMIN, TAMZMAX):
    array = np.zeros([TAM * TAMBLOCK, TAM * TAMBLOCK, RGB], dtype=np.uint8)
    for x in range(TAMBLOCK):
        for y in range(TAMBLOCK):
            if z < 10:
                filename = "./teste/00" + str(x) + "00" + str(y) + "0" + str(z) + ".map"
            else:
                filename = "./teste/00" + str(x) + "00" + str(y) + str(z) + ".map"
            if os.path.exists(filename):
                array_color = []
                with open(filename, "rb") as f:
                    control = 0
                    while byte := f.read(1):

                        if control >= BLOCKSIZE:
                            break
                        hex_byte = byte.hex()
                        if hex_byte not in array_color_unique:
                            array_color_unique.append(hex_byte)

                        array_color.append(check_color(hex_byte))
                        control = control + 1
                f.close()

                for i in range(TAM):
                    for j in range(TAM):
                        array[y * TAM + j, x * TAM + i] = array_color[j + i * TAM]
    img = Image.fromarray(array)
    saveFileName = "D:/" + str(z) + ".png"
    img.save(saveFileName)
array_color_unique.sort()
print(array_color_unique)
