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

    if choice == 1:
        out = (256 - 1) ** (img / 255) - 1
        title = 'Exponential Transformation'
    elif choice == 2:
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
    elif choice == 3:
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
    
