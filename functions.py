import cv2
import numpy as np 

def check_rect(x,y,z):

    if((x>20 and x<100) and (y>5 and y<60)):
        return "clean"
    if((x>130 and x<210) and (y>5 and y<60)):
        return "eraser"
    if((x>240 and x<320) and (y>5 and y<60)):
        return "green"
    if((x>350 and x<430) and (y>5 and y<60)):
        return "red"
    if((x>470 and x<550) and (y>5 and y<60)):
        return "blue"
    if((x>590 and x<630) and (y>5 and y<60)):
        return "save"
    return z

def contour_operation(mask,img):
    contour,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    if len(contour)>0:
        cnt=sorted(contour,key=cv2.contourArea,reverse=True)[0]
        area=cv2.contourArea(cnt)
        if area>120:
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
            cv2.circle(img,(int(x),int(y)),int(w/2),(0,255,255),2)
    return x,y


def mask_generator(lh,ls,lv,uh,us,uv,hsv_img):
    l_value=np.array([73,115,100])
    u_value=np.array([175,255,255])
    
    mask=cv2.inRange(hsv_img,l_value,u_value)
    kernel=np.ones((5,5),np.uint8)
    cv2.erode(mask,kernel,iterations=1)
    cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    cv2.dilate(mask,kernel,iterations=1)

    return mask


def draw_rect(img):
    cv2.rectangle(img,(20,5),(100,60),(0,0,0),cv2.FILLED)
    cv2.putText(img,"ERASE ALL",(30,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,255,255),1)

    cv2.rectangle(img,(130,5),(210,60),(0,0,0),cv2.FILLED)
    cv2.putText(img,"ERASER",(140,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,255,255),1)

    cv2.rectangle(img,(240,5),(320,60),(0,255,0),cv2.FILLED)
    cv2.putText(img,"GREEN",(250,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)

    cv2.rectangle(img,(350,5),(430,60),(0,0,255),cv2.FILLED)
    cv2.putText(img,"RED",(360,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)

    cv2.rectangle(img,(470,5),(550,60),(255,0,0),cv2.FILLED)
    cv2.putText(img,"BLUE",(480,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)

    cv2.rectangle(img,(590,5),(630,60),(0,255,255),cv2.FILLED)
    cv2.putText(img,"SAVE",(595,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)
    
    return img


def track():
    lh=cv2.getTrackbarPos("LH","Setter")
    ls=cv2.getTrackbarPos("LS","Setter")
    lv=cv2.getTrackbarPos("LV","Setter")
    uh=cv2.getTrackbarPos("UH","Setter")
    us=cv2.getTrackbarPos("US","Setter")
    uv=cv2.getTrackbarPos("UV","Setter")

    return lh,ls,lv,uh,us,uv
