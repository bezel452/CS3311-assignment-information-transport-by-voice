import numpy as np
from PIL import Image

carrier = Image.open("test1.png").convert('L')
watermark = Image.open("test1_1.png").convert('1')

Layers = int(input("层(0-7):"))

carrier = np.array(carrier)
watermark = np.array(watermark)

# print(carrier)
# print(watermark)
# print(watermark.shape)
a, b = watermark.shape
a1, b1 = carrier.shape

array1 = np.zeros((a, b), dtype='float32')

for i in range(a):
    for j in range(b):
        array1[i][j] = carrier[i][j]

for i in range(a):
    for j in range(b):
        w = carrier[i][j] // (2 ** Layers)
        if w % 2 == 0 and watermark[i][j] == 1:
            carrier[i][j] = carrier[i][j] + (2 ** Layers)
        elif w % 2 == 1 and watermark[i][j] == 0:
            carrier[i][j] = carrier[i][j] - (2 ** Layers)

array2 = np.zeros((a, b), dtype='float32')
for i in range(a):
    for j in range(b):
        array2[i][j] = carrier[i][j]

I = Image.fromarray(carrier)
I.save('test1_f.png', 'PNG')

a1, b1 = carrier.shape
watermark1 = np.zeros((a1, b1), dtype='int8')

for i in range(a1):
    for j in range(b1):
        w = carrier[i][j] // (2 ** Layers)
        if w % 2 == 1:
            watermark1[i][j] = 1

watermark1.dtype = 'bool'
I = Image.fromarray(watermark1)
I.save('test1_s.png', 'PNG')

