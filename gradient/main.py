import numpy as np
import matplotlib.pyplot as plt


def lerp(v0, v1, t):
    return ((1 - t) * v0 + (t * v1))

count = 0

size = 10
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [190, 147, 197]
color2 = [123, 198, 204]

for i, v in enumerate(np.linspace(0, 1, size+size-1)):

    count += 1
    r = lerp(color1[0], color2[0], v)
    g = lerp(color1[1], color2[1], v)
    b = lerp(color1[2], color2[2], v)

    for j in range(size):
        if ((i-j) > -1) and ((i-j) < size):
            image[j][i-j] = [r, g, b]


        
figure = plt.figure(1)
plt.imshow(image)

plt.show()
