import cv2
import numpy
import time
class Detector():
    detections=[]
    img = None
    setimg = None
    newdet = False
    running = True  

    def  __init__(self):
        return
    
    def start(self):
        #while self.running:
        if self.setimg is not None:
            self.img=self.setimg
            self.setimg = None
            self.detections=[]
            self.newdet = False
            self.run()
            time.sleep(0.2)
        
    def set(self, image):
        self.setimg = image
        return

    def get(self):
        if self.newdet:
            self.newdet = False
            print('this thing is true')
            return True, self.detections
        return False, []


    def draw(self,image):
        color=(0,0,255)
        print(self.detections)
        for d in self.detections:
            x,y=d[0][0:2] 
            w,h=d[1][0:2]
            l = x - (w/2) 
            r = x + (w/2)
            t = y - (h/2) 
            b = y + (h/2)
            l = int(l)
            r = int(r)
            t = int(t)
            b = int(b)
            image = cv2.rectangle(image,(l,t),(r,b),color = color,thickness=2)
        return image
    
    def close(self):
        self.running = False
        return
