import cv2
from picamera2 import Picamera2
from libcamera import controls
import time

name = 'guy' #replace with your name

picam2 = Picamera2()
picam2.preview_configuration.main.size=(512,304)
picam2.preview_configuration.main.format="RGB888"
picam2.preview_configuration.controls.FrameRate=25
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})

fps=0
img_counter=0
while True:
    tStart=time.time()
    frame=picam2.capture_array()
    # cv2.putText(frame, str(int(fps))+' fps', (30,60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3)
    cv2.imshow("piCam", frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break;
    elif k==ord(' '):
        img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
    fps=.9*fps + .1*(1/(time.time()-tStart))
    #print(int(fps))
cv2.destroyAllWindows()