import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def main():
    source = io.imread('source.png')
    print(f'type: {type(source)}')  # np.ndarray
    print(f'shage: {source.shape}')
    print(f'size: {source.size / (1 << 20):.2f} MB')
    image = source[:, :, 0].copy()
    for i in range(8)[::-1]:
        layer = 1 << i
        mask = image > layer
        image[mask] -= layer
        plt.imsave(f'layer{layer}.png', image, cmap='gray')
        print(f'layer{layer} saved')

    # image[mask] = 255
    # image[~mask] = 0
    # image[100:200, 100:200, :] = 0
    # plt.imshow(image, cmap='gray')


if __name__ == '__main__':
    print('main')
    main()
    plt.show()
