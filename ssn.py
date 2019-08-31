from numpy import uint8
from skimage import io
import matplotlib.pyplot as plt


def disassemble():
    print('disassembling')
    source = io.imread('source.png')
    print(f'type: {type(source)}')
    print(f'shage: {source.shape}')
    print(f'size: {source.size / (1 << 20):.2f} MB')
    image = source[:, :, :].copy()
    for i in range(8)[::-1]:
        layer = 1 << i
        mask = image >= layer
        image[mask] -= layer
        mask = mask.astype(dtype=uint8)*uint8(255)
        plt.imsave(f'layer{layer}.png', mask)
        print(f'layer{layer} saved')


def assemble():
    print('assembling')
    source = None
    for i in range(8)[::-1]:
        layer = 1 << i
        def load(): return io.imread(
            f'layer{layer}.png').astype(bool) * uint8(layer)
        if source is None:
            source = load()
        else:
            source += load()
        plt.imsave(f'asm{(1 << 8) - (1 << i)}.png', source)
        print(f'layer{layer} embedded')
    plt.imshow(source)  # , cmap='gray')
    plt.imsave('composed.png', source)


def main():
    disassemble()
    assemble()


if __name__ == '__main__':
    print('main')
    main()
    plt.show()
