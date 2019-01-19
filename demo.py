import numpy as np
import cv2
cap = cv2.VideoCapture('E:/广东爱情故事.mp4')
fps = int(cap.get(cv2.CAP_PROP_FPS))
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(* 'XVID')
out = cv2.VideoWriter('output.avi',fourcc,fps,size)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
