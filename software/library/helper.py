import sys
import matplotlib.pyplot as plt

# import custom libraries
sys.path.append("library")
from contrast_transform     import contrast_transform
from segmentation_transform import segmentation_transform
from morphologic_transform  import morphologic_transform

# function to return the pathology for the selected image
def returnPathologyForImage(img_name, imageInfoList):
    for i in imageInfoList:
        if img_name in i:
            
            i = i.split()
            if (len(i) > 3):        
                if(i[3] == 'B'):
                    print('benign')
                
                elif(i[3] == 'M'):
                    print('malign')
            else:
                print('normal')

# function to run a certain library transformation
def runPipelineSegment(seg_no, img_in):
    img_out_list = []
    if seg_no == 1:
        for transform_number in range(1,4):
            img_out, title = contrast_transform(img_in, transform_number)
            img_out_list.append(img_out)
            plt.figure()
            plt.imshow(img_out, cmap = 'gray')
            plt.title(transform_number)
    
    elif seg_no == 2:
        for transform_number in range(1,4):
            img_out = segmentation_transform(img_in, transform_number)
            img_out_list.append(img_out)
            plt.figure()
            plt.imshow(img_out, cmap = 'gray')
            plt.title(transform_number)
    
    elif seg_no == 3:
        for transform_number in range(1,4):
            img_out = morphologic_transform(img_in, transform_number)
            img_out_list.append(img_out)
            plt.figure()
            plt.imshow(img_out, cmap = 'gray')
            plt.title(transform_number)
            
    return img_out_list