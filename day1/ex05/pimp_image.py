import numpy as np
from numpy import ndarray as array
import sys
from load_image import ft_show

def ft_invert(array: array) -> array:
    """Inverts the color of the image received"""
    try:
        new_img = 255 - array.copy()
        ft_show(new_img, "Invert")
        return new_img

    except Exception as e:
        print("Error:", e)
        sys.exit()


def ft_red(array: array) -> array:
    """Only gets red channel for image"""
    try:
        new_img = array.copy()
        new_img[:, :, 1] = 0
        new_img[:, :, 2] = 0
        ft_show(new_img, "Red")
        return new_img

    except Exception as e:
        print("Error:", e)
        sys.exit()


def ft_green(array: array) -> array:
    """Only gets green channel for image"""
    try:
        new_img = array.copy()
        new_img[:, :, 0] = 0
        new_img[:, :, 2] = 0
        ft_show(new_img, "Green")
        return new_img

    except Exception as e:
        print("Error:", e)
        sys.exit()



def ft_blue(array: array) -> array:
    """Only gets blue channel for image"""
    try:
        new_img = array.copy()
        new_img[:, :, 0] = 0
        new_img[:, :, 1] = 0
        ft_show(new_img, "Blue")
        return new_img

    except Exception as e:
        print("Error:", e)
        sys.exit()



def ft_grey(array: array) -> array:
    """Converts image to grayscale"""
    try:
        new_img = array.copy()
        newArr = (new_img.sum(axis=2) / 3).astype(np.uint8)
        ft_show(new_img, "Grey")
        return new_img

    except Exception as e:
        print("Error:", e)
        sys.exit()
