#!/usr/bin/python3

import sys
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(img_list: np.ndarray, startX: int, startY: int, lenX: int,
            lenY: int) -> np.ndarray:
    "Takes a 2D list of RBG values of an image and return a slice of it"
    return img_list[startY:startY + lenY, startX:startX + lenX, 0:1]


def ft_rotate(img_list: np.ndarray) -> np.ndarray:
    """Transposes a 2D array"""
    assert len(img_list.shape) == 2, "Not a 2 dimensional array."
    new_img = np.rot90(img_list, k=1)

    return new_img


def main():
    """The main function to test function ft_load"""
    try:
        img_list = ft_load("animal.jpeg")
        if img_list is None:
            sys.exit(1)
        print(img_list)
        new_img_list = ft_zoom(img_list, 450, 100, 400, 400)
        print("New shape after slicing:", new_img_list.shape)
        print(new_img_list)

        new_img = ft_rotate(new_img_list.squeeze())
        print("New shape after Transpose:", new_img.shape)
        print(new_img)
        plt.imshow(new_img, cmap="gray")
        plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
