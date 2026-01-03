import pyautogui
import cv2 as cv
import numpy as np
import time


def get_coords():
    x_list = []
    y_list = []
    
    start = time.time()
    
    while time.time() - start < 6:
        x, y = pyautogui.position()
        x_list.append(x)
        y_list.append(y)
        time.sleep(0.5)
    
    x_arr = np.array(x_list)
    y_arr = np.array(y_list)
    
    return np.mean(x_arr), np.mean(y_arr)

def dynamic_kernel(min_dim:int):
    if min_dim < 200:
        factor = 0.01  #small canva -> thick edges
    elif min_dim < 500:
        factor = 0.007 #medium -> slighly thick
    elif min_dim < 1000:
        factor = 0.005  # big -> normal
    else:
        factor = 0.003  #huge -> thin
    k = max(1,int(min_dim*factor))
    return np.ones((k,k), np.uint8)


def auto_canny(img,kernel):
    #range of canny and dilate to achieve
    target_min=0.01
    target_max=0.08
    
    start_high=500
    step=20
    max_steps=20

    #to track pixels
    total_pixels=img.shape[0]*img.shape[1]
    high=start_high

    for _ in range(max_steps):
        #trying threesolds
        low=max(10,high//3)
        edges=cv.Canny(img,low,high)
        edges=cv.dilate(edges,kernel,iterations=1)

        edges_pixel=np.count_nonzero(edges)
        #to be sure it doesn't crash
        if edges_pixel==0:
            high-=step
            continue

        ratio=edges_pixel/total_pixels

        if ratio<target_min:
            high-=step
        elif ratio>target_max:
            high+=step
        else:
            break

        high=max(50,min(high,1000))

    return edges,low,high,ratio







def clean_image(img):
    #top left
    print("\nReading top left coordinates, keep the cursor still please")
    x1,y1 = get_coords()
    #bottom right
    print("Reading bottom right coordinates, keep the cursor still please")
    x2,y2= get_coords()
    
    print("Read successfully")
    #calculate the height and width of the canva
    h_canvas = abs(y1-y2)
    w_canvas = abs(x2-x1)
    
    #get height and width of the image
    y_img, x_img = img.shape[:2]

    #resizing it so we're sure it doesn't get out of the canvas
    
    #nested min because the img could be smaller than the canva
    scale = min(1.0, min(w_canvas/x_img, h_canvas/y_img))
    final_x = int(x_img*scale)
    final_y = int(y_img*scale)
    img = cv.resize(img, (final_x, final_y))
    
    #find the best kernel setting
    dim_min = min(final_x,final_y)
    kernel = dynamic_kernel(dim_min)
    
    edges = auto_canny(img,kernel)[0]
    return edges, final_x, final_y, x1,y1


