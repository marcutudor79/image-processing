# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:05:22 2023

@author: elena
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2 

def segmentation_transform(img, choice):
    
    # Segmentation 
    if choice == 1:    
        
        Tb = 255
        a = 50  # a needed very low 
        b = 200
        
        img = img.astype('float')
        s = img.shape   
        out = np.zeros((s[0],s[1]), dtype = 'uint8')
        
        for i in range(s[0]):
            for j in range(s[1]):
                if (img[i,j] < a):
                    out[i,j] = 0
                elif img[i,j] >= a and img[i,j] < b:
                    out[i,j] = Tb 
                else:
                    out[i,j] = 0
    
        plt.figure()
        plt.subplot(1,2,1), plt.imshow(img, cmap = 'gray'), plt.title('original_photo')
        plt.subplot(1,2,2), plt.imshow(out, cmap = 'gray'), plt.title('slicing_transf') 

    # Binary
    elif choice == 2:
        
        s = img.shape
        out = np.zeros((s[0],s[1]), dtype = 'uint8')
        prag = 60
        for i in range(s[0]):
            for j in range(s[1]):
                if (img[i,j] < prag):
                    out[i,j] = 0
                else:
                    out[i,j] = 255

        plt.figure()
        plt.subplot(1,2,1), plt.imshow(img, cmap = 'gray'), plt.title('Original_photo')
        plt.subplot(1,2,2), plt.imshow(out, cmap = 'gray'), plt.title('binarization_transf')  
    
    # Otsu transformation
    else:
        # gray level needs to be ensured 'uint8'.
        img = img.astype("uint8")
        
        # applying Otsu thresholding 
        # as an extra flag in binary  
        # thresholding      
        ret, thresh1 = cv2.threshold(img, 0, 255,  cv2.THRESH_OTSU)      
          
        # the window showing output image          
        # with the corresponding thresholding          
        # techniques applied to the input image     
        plt.figure()
        plt.subplot(1,2,1), plt.imshow(img, cmap = 'gray'), plt.title('Original_photo')
        plt.subplot(1,2,2), plt.imshow(thresh1, cmap = 'gray'), plt.title('Otsu_transf')    
              
        # De-allocate any associated memory usage          
        if cv2.waitKey(0) & 0xff == 27: 
            cv2.destroyAllWindows()  
 