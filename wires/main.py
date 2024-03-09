from skimage.measure import label
from skimage.morphology import (binary_closing, binary_dilation, binary_opening, binary_erosion)
import matplotlib.pyplot as plt
import numpy as np

images = [np.load("wires1npy.txt"), np.load("wires2npy.txt"), np.load("wires3npy.txt"), np.load("wires4npy.txt"),np.load("wires5npy.txt"),np.load("wires6npy.txt")]
count = 1

for image in images:
    
    labeled = label(image)
    print(f"\nИзображение {count}")
    
    print(f"Количество проводов: {labeled.max()}")

    for x in range(1, labeled.max()+1):
        labeled_erosioned = label(binary_erosion((labeled == x)))
        num_of_parts = labeled_erosioned.max()

        if num_of_parts == 0:
            num_of_parts = 1
            
        print(f"Количество частей в проводе {x}: {num_of_parts}")

    count+= 1

    plt.imshow(image)
    plt.show()
