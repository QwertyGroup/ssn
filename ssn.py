from skimage import data, filters
import matplotlib.pyplot as plt


def main():
    print('main')
    image = data.coins()   # ... or any other NumPy array!
    edges = filters.sobel(image)
    plt.imshow(edges, cmap='gray')


if __name__ == '__main__':
    main()