#Module function: provide the function to generate and process the position matrix. The disc positions in the sticks are managed like a matrix.
#Functions: get_detected_matrix, bot in char and numbers. Compare_matrix: compares the theorical (from global variables in settingsHD.py) and the detected matrix, returns a boolean  


import numpy as np

#my custom modules imports
import settingsHD as glb #this import all the global variables

#------------------------------------------------------------------------------------
#This function detemines the detected matrix (the actual matrix that is 'seen' by the camera). The detected matrix is really the disc position.
#Structure: 3x3. 3 rows determine for this game the quantity of discs. 3 columns determines the quantity of the columns.
#Input: the dictonary that is created by the function detect_color from the module hanoi_img_proc. This dictonary uses char variables to name each dics.
#Output: the 3x3 matrix where the elements are the char first letter of the discs: Yellow, Blue, Red. For positions where are no discs, the char is 0.


def get_detected_matrix_char(sort_dict):
    #local variables
    detection_matrix = np.zeros((3,3), dtype = str)
    
    for n in range (0,3):
        sort = sort_dict['sort' + str(n)]
        for j in range (0,3):
            if sort[j][1] == 0:
                detection_matrix[j][n] = 0
            else:
                detection_matrix[j][n] = sort[j][0] 
    return detection_matrix  


#------------------------------------------------------------------------------------
#This function detemines the detected matrix (the actual matrix that is 'seen' by the camera). The detected matrix is really the disc position.
#Structure: 3x3. 3 rows determine for this game the quantity of discs. 3 columns determines the quantity of the columns.
#Input: the dictonary that is created by the function detect_color from the module hanoi_img_proc. This dictonary uses integer variables to name each dics.
#Output: the 3x3 matrix where the elements are the converted to numbers: 1-Blue, 2-Yellow,  3-Red. The greater the number, greater the disc. For positions where are no discs, the char is 0.


def get_detected_matrix_num(sort_dict):
    #local variables
    detection_matrix = np.zeros((3,3))
    
    for n in range (0,3):
        sort = sort_dict['sort' + str(n)]
        for j in range (0,3):
            if sort[j][1] == 0:
                detection_matrix[j][n] = 0
            elif sort[j][0] == 'B':
                detection_matrix[j][n] = 1
            elif sort[j][0] == 'Y':
                detection_matrix[j][n] = 2
            elif sort[j][0] == 'R':
                detection_matrix[j][n] = 3
                    
    return detection_matrix     



def compare_matrix (detected_matrix, state):
    hanoi_mat= glb.hanoi_matrix_char[(3*state):(3*(state+1)), :] #this is the theorical correct matrix
    flip_detected_matrix_char = np.fliplr(detected_matrix) #need to flip to adjust user/robot perspective
    matrices_are_equal = (flip_detected_matrix_char == hanoi_mat).all()
    return matrices_are_equal