import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def disassemble():
    print('disassembling')
    source = io.imread('source.png')
    print(f'type: {type(source)}')  # np.ndarray
    print(f'shage: {source.shape}')
    print(f'size: {source.size / (1 << 20):.2f} MB')
    image = source[:, :, 0].copy()
    # image = source[:, :, :].copy()
    for i in range(8)[::-1]:
        layer = 1 << i
        mask = image >= layer
        image[mask] -= layer
        plt.imsave(f'layer{layer}.png', mask, cmap='gray')
        print(f'layer{layer} saved')


def assemble():
    print('assembling')
    source = None
    for i in range(8)[::-1]:
        layer = 1 << i
        if source is None:
            source = io.imread(f'layer{layer}.png').astype(bool) * layer
        else:
            source += io.imread(f'layer{layer}.png').astype(bool) * layer
        print(f'layer{layer} embedded')
    plt.imshow(source, cmap='gray')


def main():
    disassemble()
    assemble()


if __name__ == '__main__':
    print('main')
    main()
    plt.show()
