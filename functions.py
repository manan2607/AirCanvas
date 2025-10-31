import cv2
import numpy as np 

def clean(img,x,y):
    canvas=np.ones_like(img)*255
    return canvas

def blue(canvas,x,y): 
    cv2.circle(canvas,(x+10,y+5),8,(255,0,0),cv2.FILLED)
    return canvas

def red(canvas,x,y):
    cv2.circle(canvas,(x+10,y+5),8,(0,0,255),cv2.FILLED)
    return canvas

def blur(img):
    blur_img=cv2.GaussianBlur(img,(11,11),0)
    return blur_img

def eraser(canvas,x,y):
    cv2.circle(canvas,(x+10,y+5),24,(255,255,255),cv2.FILLED)
    return canvas

def green(canvas,x,y):
    cv2.circle(canvas,(x+10,y+5),8,(0,255,0),cv2.FILLED)
    return canvas

def write_file(a):
    f=open("mode.txt","w+")
    f.write(a)
    f.close()

def read_file():
    f=open("mode.txt","r+")
    a=f.read()
    f.close()
    return a

def check_rect(x,y):
    if((x>20 and x<100) and (y>5 and y<60)):
        write_file("clean")
    if((x>130 and x<210) and (y>5 and y<60)):
        write_file("eraser")
    if((x>240 and x<320) and (y>5 and y<60)):
        write_file("green")
    if((x>350 and x<430) and (y>5 and y<60)):
        write_file("red")
    if((x>470 and x<550) and (y>5 and y<60)):
        write_file("blue")
    if((x>590 and x<630) and (y>5 and y<60)):
        write_file("save")
    else:
        pass

def contour_operatio(mask,img):
    contour,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    a=(0,0)
    for cnt in contour:
        area=cv2.contourArea(cnt)
        if area>170:
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
            cv2.circle(img,(x+10,y+5),8,(0,255,0),5)
    return x,y

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

def hsv(blur_img):
    hsv_img=cv2.cvtColor(blur_img,cv2.COLOR_BGR2HSV)
    return hsv_img

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

