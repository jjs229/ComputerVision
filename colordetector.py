from xml.dom import NoModificationAllowedErr
from detector import Detector
import cv2
class ColorDetector(Detector):

    img = None
    newdet = False
    running = True


    def run(self):
        while self.running == None:
            if self.img is not None:
                image = self.img
                self.img = None
                self.detections=[]
                hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
                thresh = cv2.blur(cv2.inRange(hsv,(20,120,120),(255,255,255), cv2.THRESH_BINARY), (50,50))
                cv2.imshow("thimage", thresh)
                #color wheel code
                contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for c in contours:
                ##   if cv2.contourArea()
                #      continue
                    l, r, w, h = cv2.boundingRect(c)
                    x = l + (w//2)
                    y = r + (h/2) 
                    pos = [x, y, 1]
                    size = [w, h, 1]
                    self.detections += [[pos, size]]
                    #print(pos, size)
                
                return self.detections
                #box = c.bounding_box
                #l, t, r, b = box
                #pos = [(l+r)/2+l,(t+b)/2 + t,1]
                #scale = [abs((r-l)),abs((b-t)),1]
                #self.detections=[pos,scale]
                #return self.detections
