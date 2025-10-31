import numpy as np
import cv2
import time
from functions import blur, hsv, mask_generator, track, draw_rect, contour_operation, check_rect, read_file, clean, green, eraser, red, blue, write_file


paint=True
er=False
status="draw"
f=open("mode.txt","w+")
f.write("clean")
f.close()

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
cv2.createTrackbar("LH","Setter",0,179,nothing)
cv2.createTrackbar("LS","Setter",0,255,nothing)
cv2.createTrackbar("LV","Setter",0,255,nothing)
cv2.createTrackbar("UH","Setter",179,179,nothing)
cv2.createTrackbar("US","Setter",255,255,nothing)
cv2.createTrackbar("UV","Setter",255,255,nothing)



while True:
    _,img=video.read()
    img=cv2.flip(img,1)
    
    blur_img=blur(img)
    hsv_img=hsv(blur_img)
    lh,ls,lv,uh,us,uv=track()
    mask=mask_generator(lh,ls,lv,uh,us,uv,hsv_img)
    img=draw_rect(img)
    x,y=contour_operation(mask,img)

    check_rect(x,y)

    status=read_file()

    

    if status=="clean":
        canvas=clean(canvas,x,y)
    if status=="green":
        canvas=green(canvas,x,y)
    if status=="eraser":
        canvas=eraser(canvas,x,y)
    if status=="red":
        canvas=red(canvas,x,y)
    if status=="blue":
        canvas=blue(canvas,x,y)
    if status=="save":
        cv2.imwrite("img/pic.jpg",canvas)
        time.sleep(0.4)
        write_file("clean")


    
    op=cv2.hconcat([img,canvas])

    cv2.imshow("COMBO",op)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
        
        
video.release()
cv2.destroyAllWindows()

