#Module function: provide the functions that uses actively opencv to detect the discs and use the camera to get the ROI. 
#This is the final module created for the HANOI DROID CAPSTONE at Camosun College term Fall 2023
#this module has the following functions:

#detect_color(image_hsv): detect and classifies the disc detection in each stick
#take_one_frame(): takes the big frame that will by sectioned 
#for development details, see the notebook: disc_det_v1.ipynb and take_one_frame.ipynb
#created on june 25 - 2023


import cv2
import numpy as np

import settingsHD as glb #this import all the global variables

#glb.init()


L_limit_blue = glb.L_limit_blue
U_limit_blue = glb.U_limit_blue   

L_limit_red1 = glb.L_limit_red1
U_limit_red1 = glb.U_limit_red1 
L_limit_red2 = glb.L_limit_red2
U_limit_red2 = glb.U_limit_red2
    
L_limit_yellow  = glb.L_limit_yellow
U_limit_yellow  = glb.U_limit_yellow

mask_height = glb.mask_height
mask_width = glb.mask_width



#------------------------------------------------------------------------------------------------------------
#this function is used to take the big frame or the big sreen, one shot, that will be processed extracting the smaller frame and mini-frames
#input: nothing
#output: the frame captured by the webcam
#challenges: to improve: the videocapture uses the channel 0, sometimes this could change, maybe a for loop could seewp or another method to get the exact webcam channel number.



def take_one_frame():

    cap = cv2.VideoCapture(1)   #id for the disc camera is one

    #check if connection with camera is successfully
    if cap.isOpened():
        ret, frame = cap.read()  #capture a frame from live video

        #check whether frame is successfully captured
        if ret:
            print("Frame taken")
            cap.release()
        #print error if frame capturing was unsuccessful
        else:
            print("Error : Failed to capture frame")

    # print error if the connection with camera is unsuccessful
    else:
        print("Cannot open camera")
    
    return frame
    
    
    
    
    
    #------------------------------------------------------------------------------------------------------------
#this function is used to take the big frame or the big sreen, one shot, that will be processed extracting the smaller frame and mini-frames
#input: nothing
#output: the frame captured by the webcam
#challenges: to improve: the videocapture uses the channel 0, sometimes this could change, maybe a for loop could seewp or another method to get the exact webcam channel number.

def convert_and_crop(img):

    imagehsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert the big frame to HSV
    imagehsvcopy = imagehsv.copy()
    small_image_hsv = imagehsvcopy[130:230, 0:630] #crop to adjust the desire ROI
    
    
    return small_image_hsv
    

#----------------------------------------------------------------------------------------------------------------------------
#This function is use to process the rectangle section of each stick and process looking for the colors of the disc
# Input parameter: the small rectangle that corresponds to the stick in detail. only one stick miniframe at time
# Output: the output is an array that contains the position in pixels of the disc yellow, blue and red. If the position is 0, then, no disc of this color is detected.

def detect_color(image_hsv):
   
    #local variables

    # flags that determine the detection of a disc
    b_disc_flag = False   
    r_disc_flag = False  
    y_disc_flag = False

    #variables to store the total of pixels find for specific color
    b_pixels_total = 0
    b_pixels_acum =  0
    r_pixels_total = 0
    r_pixels_acum =  0
    y_pixels_total = 0
    y_pixels_acum =  0



    #number of the row that is determined for the disc position

    b_row = 0
    r_row = 0
    y_row = 0

    
    #this is to find the colors in the mask, using the function inRange. To see the real color, the bitwise is used, because inRange returns only 0 and 255 to be masked
    b_mask=cv2.inRange(image_hsv,L_limit_blue,U_limit_blue)
    #blue=cv2.bitwise_and(image2,image2,mask=b_mask) #this is optional, only for visualization

    r_mask1=cv2.inRange(image_hsv,L_limit_red1,U_limit_red1) #in the map, the red has 2 sections
    r_mask2=cv2.inRange(image_hsv,L_limit_red2,U_limit_red2)
    r_mask = r_mask1 + r_mask2
    #red=cv2.bitwise_and(image2,image2,mask=r_mask)    #this is optional, only for visualization



    y_mask=cv2.inRange(image_hsv,L_limit_yellow,U_limit_yellow)
    #yellow=cv2.bitwise_and(image2,image2, mask=y_mask)  #this is optional, only for visualization

    #convert the mask from the 255 values to 1, i think more easy to count pixels.
    b_mask = b_mask/255
    r_mask = r_mask/255
    y_mask = y_mask/255
    
    b_pixels_total = b_mask.sum()
    r_pixels_total = r_mask.sum()
    y_pixels_total = y_mask.sum()

    #if I have a certain threshold value of pixels, I could determine that I have a disc of that specific value.
    if b_pixels_total > 175:
        b_disc_flag = True

    if r_pixels_total > 175:
        r_disc_flag = True
   

    if y_pixels_total > 175:
        y_disc_flag = True    
        
#then, if I have a flag for a specific disc, I must search its position in the mask, from top to down.

    if b_disc_flag:

        for i in range (0, mask_height):
            b_pixels_acum += b_mask[i].sum() 
            b_row = i

            if b_pixels_acum > 175:
                b_pixels_acum = 0  #pilas que esto es lo nuevo, no se si funcione
                break

    if r_disc_flag:

        for i in range (0, mask_height):
            r_pixels_acum += r_mask[i].sum() 
            r_row = i

            if r_pixels_acum > 175:
                r_pixels_acum = 0 #pilas que esto es lo nuevo
                break    


    if y_disc_flag:

        for i in range (0, mask_height):
            y_pixels_acum += y_mask[i].sum() 
            y_row = i

            if y_pixels_acum > 175:
                y_pixels_acum = 0 #pilas que esto es lo nuevo
                break  

    sort = [['Y', y_row],['B', b_row],['R', r_row]] 
    sort = sorted(sort, key=lambda x: x[1])
    return sort
        

