#!/usr/bin/python3

import sys
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(img_list: np.ndarray, startX: int, startY: int, lenX: int,
            lenY: int) -> np.ndarray:
    "Takes a 2D list of RBG values of an image and return a slice of it"
    return img_list[startY:startY + lenY, startX:startX + lenX, 0:1]


def ft_rotate(imt_list: np.ndarray) -> ndarray:
    """Transposes a 2D array"""
    assert len(img_list.shape) == 2, "Not a 2 dimensional array."
    newArray = np.zeros(imgArr.shape[::-1], np.int32)

    for i, line in enumerate(newArray):
        for j in range(len(line)):
            newArray[i][j] = imgArr[j][i]
    return newArray


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

        plt.imshow(new_img_list, cmap="gray")
        plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
