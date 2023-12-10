# import py libraries
import sys
import matplotlib.pyplot as plt
sys.path.append("library")

# import custom library
import helper as hp

# make a list db with image info
imageInfoList = [];
with open('../breastcancer_database/Info.txt') as f:
    
    # list containing lines of file
    lines = f.readlines()

    for line in lines:
        # remove leading/trailing white spaces
        line = line.strip()
        
        # append dictionary to list
        imageInfoList.append(line) 

def main():
    
    # FIRST IMAGE
    # running mdb003 through the transformation pipeline
    path     = r'../breastcancer_database/mdb003.pgm'
    img_in   = plt.imread(path)
    img_out_list = []
    
    # run contast_transform library
    img_out_list = hp.runPipelineSegment(1, img_in);
    plt.show()
    
    # let user to make a choice 
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # run segmentation_transform library
    img_out_list = hp.runPipelineSegment(2, img_out_list[user_choice - 1])
    plt.show()
    
    # let user to make a choice 
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # run morphologic_transform library
    img_out_list = hp.runPipelineSegment(3, img_out_list[user_choice - 1])
    plt.show()
    
    # let user make a choice
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # show the final result and the pathology based on the Info.txt
    plt.figure()
    plt.imshow(img_out_list[user_choice - 1], cmap = 'gray')
    plt.show()
    hp.returnPathologyForImage('mdb003', imageInfoList)
    
    
    # SECOND IMAGE
    # running mdb0028 through the transformation pipeline
    path     = r'../breastcancer_database/mdb028.pgm'
    img_in   = plt.imread(path)
    img_out_list = []
    
    # run contast_transform library
    img_out_list = hp.runPipelineSegment(1, img_in);
    plt.show()
    
    # let user to make a choice 
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # run segmentation_transform library
    img_out_list = hp.runPipelineSegment(2, img_out_list[user_choice - 1])
    plt.show()
    
    # let user to make a choice 
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # run morphologic_transform library
    img_out_list = hp.runPipelineSegment(3, img_out_list[user_choice - 1])
    plt.show()
    
    # let user make a choice
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # show the final result and the pathology based on the Info.txt
    plt.figure()
    plt.imshow(img_out_list[user_choice - 1], cmap = 'gray')
    plt.show()
    hp.returnPathologyForImage('mdb028', imageInfoList)
    
    # THIRD IMAGE
    # running mdb099 through the transformation pipeline
    path     = r'../breastcancer_database/mdb099.pgm'
    img_in   = plt.imread(path)
    img_out_list = []
    
    # run contast_transform library
    img_out_list = hp.runPipelineSegment(1, img_in);
    plt.show()
    
    # let user to make a choice 
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # run segmentation_transform library
    img_out_list = hp.runPipelineSegment(2, img_out_list[user_choice - 1])
    plt.show()
    
    # let user to make a choice 
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # run morphologic_transform library
    img_out_list = hp.runPipelineSegment(3, img_out_list[user_choice - 1])
    plt.show()
    
    # let user make a choice
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # show the final result and the pathology based on the Info.txt
    plt.figure()
    plt.imshow(img_out_list[user_choice - 1], cmap = 'gray')
    plt.show()
    hp.returnPathologyForImage('mdb099', imageInfoList)
    
    
    # FOURTH IMAGE
    # running mdb021 through the transformation pipeline
    path     = r'../breastcancer_database/mdb021.pgm'
    img_in   = plt.imread(path)
    img_out_list = []
    
    # run contast_transform library
    img_out_list = hp.runPipelineSegment(1, img_in);
    plt.show()
    
    # let user to make a choice 
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # run segmentation_transform library
    img_out_list = hp.runPipelineSegment(2, img_out_list[user_choice - 1])
    plt.show()
    
    # let user to make a choice 
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # run morphologic_transform library
    img_out_list = hp.runPipelineSegment(3, img_out_list[user_choice - 1])
    plt.show()
    
    # let user make a choice
    user_choice = int(input('Choose an image from 1 to 3 \n'))
    
    # show the final result and the pathology based on the Info.txt
    plt.figure()
    plt.imshow(img_out_list[user_choice - 1], cmap = 'gray')
    plt.show()
    hp.returnPathologyForImage('mdb021', imageInfoList)

# run the program     
if __name__ == "__main__":
    main()