from detector import Detector
import cv2
import time
class MotionDetector(Detector):

    prvs = None

    def run(self):
        self.detections=[]
        nxt = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        if self.prvs is None:
            self.prvs = nxt
        flow = cv2.calcOpticalFlowFarneback(self.prvs,nxt,None, 0.5, 3, 15, 3, 5, 1.2, 0) #finish this
        self.prvs = nxt
        mag, _ =cv2.cartToPolar(flow[...,0], flow[...,1]) #finish this
        blur = cv2.blur(mag, (50,50))
        thresh0 = cv2.inRange(blur, 0.56, 50)
        thresh = cv2.blur(thresh0, (40,40))
        #cv2.imshow('raw', mag)
        #cv2.imshow('blur', blur)
        #cv2.imshow('blurthresh', thresh0)
        #cv2.imshow('blurthreshblur', thresh)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.createtrackbar

        for c in contours:
            l, r, w, h = cv2.boundingRect(c)
            if w*h <= 1000: #700k is crazy high, find real number
                continue 
            x = l + (w//2)
            y = r + (h/2) 
            pos = [x, y, 1]
            size = [w, h, 1]
            self.detections += [[pos, size]]
            self.newdet = True
            #print(pos, size)
        return self.newdet, self.detections
                #box = c.bounding_box
                #l, t, r, b = box
                #pos = [(l+r)/2+l,(t+b)/2 + t,1]
                #scale = [abs((r-l)),abs((b-t)),1]
                #self.detections=[pos,scale]
                #return self.detections
        
