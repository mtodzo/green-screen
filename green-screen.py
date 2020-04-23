import importlib
import numpy as np
import matplotlib.pyplot as plt
import cv2

def green_screen(image, green_scrn_val):
    print(image)


if __name__ == "__main__":
    im = cv2.imread('miles.jpg')
    print(im)
    green_scrn_val = input("Green screen value? ")
    green_screen(im, green_scrn_val)
