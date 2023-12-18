#settingsHD.py: created specifically for the postions of the platforms of the Hanoi Droid Capstone.
#Camosun college Term Fall 2023

import numpy as np


#This is the square size of the ROI and x,y coordinates positions
    
mask_width = 50
mask_height = 60

mask_x_position_dict = {'x0' : 90, 'x1': 260, 'x2' : 470}  
mask_y_position_dict = {'y0' : 20, 'y1': 5, 'y2' : 10}  
    
    
    
    #the color ranges, this is setting experimentally but should be improved or looking for a theorical approach

    
    ##------ BLUE----------


L_limit_blue=np.array([98,50,10]) # setting the blue lower limit  ----change the V from 50 to 10 after testing dec13
U_limit_blue=np.array([139,255,255]) # setting the blue upper limit

    ##------ RED----------


L_limit_red1=np.array([0,50,50]) # setting the red part1 lower limit
U_limit_red1=np.array([10,255,255]) # setting the red part1 upper limit
L_limit_red2=np.array([160,50,50]) # setting the red part1 lower limit
U_limit_red2=np.array([179,255,255]) # setting the red part1 upper limit
    
    
       ##------ YELLOW----------
  

L_limit_yellow=np.array([19,100,50]) # setting the yellow lower limit
U_limit_yellow=np.array([25,255,255]) # setting the yellow upper limit



   ##--------Fixed disc positions and movements represented as matrix
    
    
hanoi_matrix_num = np.zeros((3,3))
hanoi_matrix_num = np.array([[3, 0, 0 ], [2, 0, 0 ], [1, 0, 0], 
                            [0, 0, 0 ], [2, 0, 0 ], [1, 0, 3],
                            [0, 0, 0 ], [0, 0, 0 ], [1, 2, 3],
                            [0, 0, 0 ], [0, 3, 0 ], [1, 2, 0],
                            [0, 0, 0 ], [0, 3, 0 ], [0, 2, 1],
                            [0, 0, 0 ], [0, 0, 0 ], [3, 2, 1],
                            [0, 0, 0 ], [0, 0, 2 ], [3, 0, 1],
                            [0, 0, 3 ], [0, 0, 2 ], [0, 0, 1]]) 
    
    
    
   
hanoi_matrix_char = np.zeros((3,3), dtype = str)
hanoi_matrix_char = np.array([['R', '0', '0' ], ['Y', '0', '0' ], ['B', '0', '0'], 
                            ['0', '0', '0' ], ['Y', '0', '0' ], ['B', '0', 'R'],
                            ['0', '0', '0' ], ['0', '0', '0' ], ['B', 'Y', 'R'],
                            ['0', '0', '0' ], ['0', 'R', '0' ], ['B', 'Y', '0'],
                            ['0', '0', '0' ], ['0', 'R', '0' ], ['0', 'Y', 'B'],
                            ['0', '0', '0' ], ['0', '0', '0' ], ['R', 'Y', 'B'],
                            ['0', '0', '0' ], ['0', '0', 'Y' ], ['R', '0', 'B'],
                            ['0', '0', 'R' ], ['0', '0', 'Y' ], ['0', '0', 'B']]) 
    


