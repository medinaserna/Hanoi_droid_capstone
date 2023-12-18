#This module is used to draw some fixed and custom windos display in the main program

import cv2
import numpy as np


def draw_intro():
    # Load four images
    image1 = cv2.imread('DATA/intro_image/intro1.png')
    image2 = cv2.imread('DATA/intro_image/intro2.png')
    image3 = cv2.imread('DATA/intro_image/intro3.png')
    image4 = cv2.imread('DATA/intro_image/intro4.png')

        # Create a 2x2 matrix with the images
    top_row = np.hstack((image1, image2))
    bottom_row = np.hstack((image3, image4))
    result = np.vstack((top_row, bottom_row))
    
    return result


def draw_error():
    # Load four images
    image1 = cv2.imread('DATA/error/error1.png')
    image2 = cv2.imread('DATA/error/error2.png')
    image3 = cv2.imread('DATA/error/error3.png')
    image4 = cv2.imread('DATA/error/error4.png')

        # Create a 2x2 matrix with the images
    top_row = np.hstack((image1, image2))
    bottom_row = np.hstack((image3, image4))
    result = np.vstack((top_row, bottom_row))
    
    return result


def draw_matrix(frame1,frame2,frame3,frame4):
    
        # Create a 2x2 matrix with the images
    top_row = np.hstack((frame1, frame2))
    bottom_row = np.hstack((frame3, frame4))
    result = np.vstack((top_row, bottom_row))
    
    return result



def draw_solved():
    # Load four images
    image1 = cv2.imread('DATA/solved/solved1.png')
    image2 = cv2.imread('DATA/solved/solved2.png')
    image3 = cv2.imread('DATA/solved/solved3.png')
    image4 = cv2.imread('DATA/solved/solved4.png')

        # Create a 2x2 matrix with the images
    top_row = np.hstack((image1, image2))
    bottom_row = np.hstack((image3, image4))
    result = np.vstack((top_row, bottom_row))
    
    
    return result


def write_in_image(image, matrix):
    
   # Choose a font and other parameters
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 2
    font_thickness = 2
    font_color = (0, 0, 255)  # Red
 
    letter_x_coord ={'x0' : 100, 'x1': 300, 'x2' : 500}
    letter_y_coord ={'y0' : 265, 'y1': 320, 'y2' : 375}



# Determine the size of the text box
#(text_width, text_height), baseline = cv2.getTextSize(text, font, font_size, font_thickness)
#x = (frame.shape[1] - text_width) // 2
#y = (frame.shape[0] + text_height) // 2

    for n in range (0,3):
        for j in range(0,3):
            cv2.putText(image, matrix[j,n], (letter_x_coord['x' + str(n)], letter_y_coord['y' + str(j)]), font, font_size, font_color, font_thickness, cv2.LINE_AA) 
    
    
    #result = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
    
    result = image.copy()
    return result
    
    