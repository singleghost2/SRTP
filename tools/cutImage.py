#coding=utf-8
import cv2
import numpy as np
import sys

video_path = sys.argv[1]
print "video path:", video_path
count=500
pixSize=20 #选框大小为2pixSize * 2pixSize

def onMouseClick(event,x,y,width,height):
    global count
    if event==cv2.EVENT_FLAG_LBUTTON:
	print "cut a hoop. Count:", count
        #cv2.rectangle(frame,(x-pixSize,y-pixSize),(x+pixSize,y+pixSize),(255,0,0),2)#绘制选框 #这行貌似可以删掉
        img=frame[y-pixSize:y+pixSize,x-pixSize:x+pixSize]#截取图片
        cv2.imwrite("positive_images/"+str(count)+".jpg",img)#保存图片
        count=count+1


videoCapture=cv2.VideoCapture(video_path)
if videoCapture.isOpened():
    totalFrameNumber=videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
    print "totalFrameNumber",totalFrameNumber
else:
    print "Video Open Error"
    sys.exit(1)
    
fps=videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
size=(int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
      int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

flag,frame=videoCapture.read()
while flag:
    cv2.imshow("video",frame)
    cv2.waitKey(1000)
    cv2.setMouseCallback("video",onMouseClick)
    if cv2.waitKey(20)&0xFF==27:#ESC键退出
        break
    
    for i in range(5):#每5帧显示？？
        flag,frame=videoCapture.read()

videoCapture.release()
cv2.destroyAllWindows()
