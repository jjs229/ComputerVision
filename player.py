import time
import cv2

class Player():
    cap= None
    dropCount = 0
    frameTime = 0
    def __init__(self,file=''): #C:/Users/H507083/Documents/Pythonschtuff/vg000006.mp4
        if file !='':
            self.cap = cv2.VideoCapture(file)
        else:
            self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            print("Stream Opened")
            cv2.namedWindow('Video Player')
        #self.cap.get(...)
        #frame rate
        #duration
        #current time  
            return
        
    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
        return
        
    def run(self):
        self.frameTime=time.time()
        return self.cap.read()
        
    def draw(self,image):
        self.frameTime = time.time()-self.frameTime
        image = cv2.putText(image,'%.2f' %(1/(0.033 + self.frameTime)),(10,50),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=2.0,color=(255,255,255),thickness=3)
        cv2.imshow('Video Player',image)
        delay = int((0.033-self.frameTime)*1000)
        if delay<1:
            delay=1
            #if dropCount>0...

        
        #put key=under
        return cv2.waitKey(delay)

#     def play():
 
#         return
 
#     def pause():
 
#         return
 
#     def rewind():
 
#         return
    #def play
    #def pause
    #def rewind
        
