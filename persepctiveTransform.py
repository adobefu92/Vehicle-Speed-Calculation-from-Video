import cv2
from win32api import GetSystemMetrics
import numpy as np

def GetReferences(frame): 
    global points
    points = list()
    
    #this function will be called whenever the mouse is double click
    def mouse_callback(event, x, y, flags, params):
        

        #the [x, y] for each double-click event will be stored here
        if event == cv2.EVENT_LBUTTONDBLCLK:
            #store the coordinates of the right-click event
            points.append([x, y])
            cv2.circle(img,(x,y),5,(255,0,0),-1)
            cv2.imshow('image', img)

            #this just verifies that the mouse data is being collected
            #you probably want to remove this later
            print (points)
            cv2.waitKey(0)

        if len(points) == 4 :
            cv2.destroyAllWindows()

    # path_image = frame
    img = frame
    scale_width = 640 / img.shape[1]
    scale_height = 480 / img.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', window_width, window_height)

    #set mouse callback function for window
    cv2.setMouseCallback('image', mouse_callback)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    points = np.float32(points)
    
    return(points)



def transform_point(point,M):
    homg_point = [point[0], point[1], 1] # homogeneous coords
    transf_homg_point = M.dot(homg_point) # transform
    transf_homg_point /= transf_homg_point[2] # scale
    transf_point = transf_homg_point[:2] # remove Cartesian coords
    transf_point = transf_point.astype(int)
#     print(transf_point)
    return(transf_point)










