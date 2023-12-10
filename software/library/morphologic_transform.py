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
    if (choice < 0 or choice > 2):
        return -1
    
    # choice 0: errosion
    if(choice == 0):
        # define a structurant element
        struct_element = np.ones((10,10))
        
        # erode image with the struct_element
        img_in = morpho.binary_erosion(img_in, struct_element)
    
    # choice 1: dilatation 
    elif(choice == 1):
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
        

# debug
path = r'mdb021.pgm' 
img  = plt.imread(path)
plt.figure()
plt.imshow(img, cmap = 'gray')

# binarize image
prag                = 150
img_bi              = np.zeros(img.shape, dtype = 'uint8')
img_bi[img >= prag] = 255
plt.figure()
plt.imshow(img_bi, cmap = 'gray')

# test function choice 0  
img = morphologic_transform(img_bi, 0)
plt.figure()
plt.imshow(img, cmap = 'gray')

# test function choice 1
img = morphologic_transform(img_bi, 1)
plt.figure()
plt.imshow(img, cmap = 'gray')

# test function choice 2
img = morphologic_transform(img_bi, 2)
plt.figure()
plt.imshow(img, cmap = 'gray')
   
   


        
    
    
    
    
    

