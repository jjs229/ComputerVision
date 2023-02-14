from detector import Detector
import cv2
import argparse

class ManualDetector(Detector):

    cropping = False
    x0 = None
    y0= None
    x1 = None
    y1= None
    def __init__(self):
        cv2.namedWindow("Video Player")
        cv2.setMouseCallback("Video Player", self.cac)

    def get(self):
        if self.newdet:
            self.newdet = False
            return True, self.detections
        return False, []

    def cac(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x0 = x
            self.y0 = y
            self.cropping = True
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates and indicate that
            # the cropping operation is finished
            self.x1 = x
            self.y1 = y
            self.cropping = False
            pos = [(self.x0 + self.x1)/2, (self.y0+self.y1)/2, 1]
            size = [abs(self.x1 - self.x0), abs(self.y1-self.y0), 1]
            self.detections = [[pos, size]]
            self.newdet = True

    def draw(self,image):
        color=(0,0,255)
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
        self.detections = []
        return image