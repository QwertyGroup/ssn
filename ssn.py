import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def main():
    image = io.imread('source.png')
    print(f'type: {type(image)}')  # np.ndarray
    print(f'shage: {image.shape}')
    print(f'size: {image.size / (1 << 20):.2f} MB')
    mask = image < 87
    image[mask] = 255
    plt.imshow(image, cmap='gray')


if __name__ == '__main__':
    print('main')
    main()
    plt.show()
