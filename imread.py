import numpy as np
import cv2
cap = cv2.VideoCapture(0)#捕获摄像头

#Define the codec and create VideoWriter object
#定义编解码器，创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:#如果获取到了视频的帧
        frame = cv2.flip(frame,0)

        #write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)&0xff == ord('q'):
            break
        else:
            break
#Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

