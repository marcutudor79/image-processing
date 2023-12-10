# necessary libraries
import matplotlib.pyplot        as plt
import numpy                    as np 
import scipy.ndimage.morphology as morpho
import cv2                      as cv


def morphologic_transform(img_in, choice):
    
    # validate input parameters
    # validation 1: image should be grayscale
    shape = img_in.shape    
    if (len(shape) != 2):
        return -1
    
    # validation 2: choice is between 0 and 2
    if (choice < 1 or choice > 3):
        return -1
    
    # choice 0: errosion
    if(choice == 1):
        # define a structurant element
        struct_element = np.ones((10,10))
        
        # erode image with the struct_element
        img_in = morpho.binary_erosion(img_in, struct_element)
    
    # choice 1: dilatation 
    elif(choice == 2):
        # define a structurant element 
        struct_element = np.ones((10,10))
        
        # dilate image with the struct_element
        img_in = morpho.binary_dilation(img_in, struct_element)
        
    # choice 2: morphological Gradient    
    else:
        # define a structurant element 
        struct_element = np.ones((10,10))
        
        # apply Morphological Gradient with the struct_element
        img_in = cv.morphologyEx(img_in, cv.MORPH_GRADIENT, struct_element)
        
     
    return img_in
        
