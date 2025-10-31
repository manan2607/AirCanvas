import numpy as np
import cv2
import time
from functions import mask_generator, track, draw_rect, contour_operation, check_rect


status="clean"
pic_no= 1

video=cv2.VideoCapture(0)
video.set(10,1000)

while True:
    check,img=video.read()
    if check==True:
        break
    
canvas=np.ones_like(img)*255

def nothing(x):
    pass

cv2.namedWindow("Setter")

trackbars = [
    ("LH", 0, 179),
    ("LS", 0, 255),
    ("LV", 0, 255),
    ("UH", 179, 179),
    ("US", 255, 255),
    ("UV", 255, 255)
]

for name, initial_val, max_val in trackbars:
    cv2.createTrackbar(name, "Setter", initial_val, max_val, nothing)


while True:
    _,img=video.read()
    img=cv2.flip(img,1)
    
    blur_img=cv2.GaussianBlur(img,(11,11),0)
    hsv_img=cv2.cvtColor(blur_img,cv2.COLOR_BGR2HSV)

    lh,ls,lv,uh,us,uv=track()

    mask=mask_generator(lh,ls,lv,uh,us,uv,hsv_img)
    img=draw_rect(img)
    x,y=contour_operation(mask,img)

    
    status=check_rect(x,y,status)

    

    if status=="clean":
        canvas=np.ones_like(img)*255
    if status=="green":
        cv2.circle(canvas,(x+10,y+5),8,(0,255,0),cv2.FILLED)
    if status=="eraser":
        cv2.circle(canvas,(x+10,y+5),24,(255,255,255),cv2.FILLED)
    if status=="red":
        cv2.circle(canvas,(x+10,y+5),8,(0,0,255),cv2.FILLED)
    if status=="blue":
        cv2.circle(canvas,(x+10,y+5),8,(255,0,0),cv2.FILLED)
    if status=="save":
        cv2.imwrite(f"img/pic{pic_no}.jpg",canvas)
        pic_no+=1
        time.sleep(0.4)
        status = "clean"


    
    op=cv2.hconcat([img,canvas])

    cv2.imshow("COMBO",op)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
        
        
video.release()
cv2.destroyAllWindows()