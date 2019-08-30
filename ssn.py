import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def main():
    image = io.imread('source.png')
    print(f'type: {type(image)}')  # np.ndarray
    print(f'shage: {image.shape}')
    print(f'size: {image.size / (1 << 20):.2f} MB')
    image = image[:,:,0]
    mask = image > 1 << 7
    image[mask] = (1 << 8) - 1
    image[~mask] = 0
    # image[100:200, 100:200, :] = 0
    plt.imshow(image, cmap='gray')


if __name__ == '__main__':
    print('main')
    main()
    plt.show()
