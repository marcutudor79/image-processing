# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:18:29 2023

@author: ZEN
"""

import numpy as np
import matplotlib.pyplot as plt

def contrast_transform(img, choice):
    s = img.shape
    out = np.zeros((s[0], s[1]), dtype='uint8')

    if choice == '1':
        out = (256 - 1) ** (img / 255) - 1
        title = 'Exponential Transformation'
    elif choice == '2':
        a, b, Ta, Tb = 100, 190, 0, 255
        for i in range(s[0]):
            for j in range(s[1]):
                if img[i, j] < a:
                    out[i, j] = Ta
                elif  img[i, j] >= a & img[i,j] < b:
                    out[i, j] = (Tb - Ta) / (b - a) * (img[i, j] - a) 
                else:
                    out[i, j] = Tb
        title = 'Contrast Stretching Transformation'
    elif choice == '3':
        a, b, Ta, Tb = 100, 170, 50, 250
        img = img.astype('float')
        for i in range(s[0]):
            for j in range(s[1]):
                if img[i, j] < a:
                    out[i, j] = (Ta / a) * img[i, j]
                else:
                    if a <= img[i, j] <= b:
                        out[i, j] = Ta + (Tb - Ta) / (b - a) * (img[i, j] - a)
                    else:
                        out[i, j] = Tb + ((255 - Tb) / (255 - b)) * (img[i, j] - b)
        out = np.clip(out, 0, 255).astype('uint8')
        title = 'Linear Transformation'
    else:
        print("Invalid transformation method.")
        return None, None

    return out, title

def main():
    path = r'mdb028.pgm'
    img = plt.imread(path)

    while True:
        transformation_choice = input("Choose transformation method (1: Exponential, 2: Contrast Stretching, 3: Linear) or 'exit' to end: ")

        if transformation_choice.lower() == 'exit':
            break

        out, title = contrast_transform(img, transformation_choice)

        if out is not None:
            plt.figure()
            plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Photo')
            plt.subplot(1, 2, 2), plt.imshow(out, cmap='gray'), plt.title(title)
            plt.show()

if __name__ == "__main__":
    main()
