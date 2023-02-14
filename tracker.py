import cv2
from cv2 import sqrt
import numpy as np
from kalmanfilterx import KalmanFilterX
import time
from trackedobject import trackedObject

class Tracker():

    pimage= None
    trackedObjects = {}
    trackid = 0
    lk_params = dict( winSize = (15, 15),maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    kp = 0.1

#This member scales throught the tracked objects and searches any matches with detections passed. It then pops any detections
#so they can stop being searched. It also logs all tracked objects and wait for the for loop to finish before removing elements
#It then appends any remaining detections to the end of the tracked objects list
    def allocate(self, det):
        temp =[]
        if self.trackedObjects:
            for id, t in self.trackedObjects.items():
                b = False
                for d in det:
                    dist =(d[0][0] - t.pos[0])**2 + (d[0][1] - t.pos[1])**2 + (d[0][2] -t.pos[2])**2
                    if dist <= 1200:
                        t = trackedObject(d)
                        b = True
                        t.newdet = True
                        yer = np.array([[np.float32(d[0][0])],[np.float32(d[0][1])],[np.float32(d[0][2])],[np.float32(d[1][0])],[np.float32(d[1][1])],[np.float32(d[1][2])]])
                        t.kal.correct(yer)#adjusts calman filter accordingly
                        det.remove(d)
                        t.tout = None
                        break
                if b!= True:
                    if not t.tout:
                        t.tout = time.time()
                    elif time.time() - t.tout >= 2:
                          temp.append(id)
            for t in temp:
                self.trackedObjects.pop(t)

            for d in det:
                self.trackid += 1
                self.trackedObjects[self.trackid] = trackedObject(d)
        else:
            for d in det:
                if self.trackid == 0:
                    self.trackedObjects[0] = trackedObject(d)
                else:
                    self.trackid +=1
                    self.trackedObjects[self.trackid] = trackedObject(d)
        return

    def set(self, det): #needs way more stuff
        self.allocate(det) #going to correct trackobjects with detections
        return
    
    def close(self):
    
        return

    def draw(self,image):
        color=(0,255,0)
        for _, t in self.trackedObjects.items():
            if t.tin >= 0.5:
                x,y=t.pos[0:2] #change index to 0:3 for z
                w,h=t.size[0:2] 
                l = int(x - (w/2))
                r = int(x + (w/2))
                t = int(y - (h/2)) 
                b = int(y + (h/2))
                image = cv2.rectangle(image,(l,t),(r,b),color = color,thickness=2)
        return

    def track(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if self.pimage == None:
            self.pimage = image
        else:
            for _, t in self.trackedObjects.items():
                if t.newdet:
                    t.p0 = cv2.goodFeaturesToTrack(image,20,0.01,10)
                    t.newdet = False
                    continue
                
                if t.p0 is not None:
                    x,y=t.pos[0:2] 
                    w,h=t.size[0:2]
                    w *= 2
                    h *= 2
                #Option 1
                    p1, st, _ = cv2.calcOpticalFlowPyrLK(self.pimage[y:y+h, x:x+w],image[y:y+h, x:x+w] , t.p0, None, **self.lk_params)
                    
                #Option 2
                    #pimagemask = np.zeros(image.shape, dtype='int32')
                    #imagemask = np.zeros(image.shape, dtype='int32')
                    #pimagemask[y:y+h, x:x+w] =pimage[y:y+h, x:x+w]
                    #imagemask[y:y+h, x:x+w] =image[y:y+h, x:x+w]
                    #p1, st, _ = cv2.calcOpticalFlowPyrLK(pimagemask[y:y+h, x:x+w],imagemask[y:y+h, x:x+w] , self.p0, None, **self.lk_params)

                    t.p0 = t.p0[st==1]
                    p1 = p1[st==1]
                    
                    dp = np.array(len(p1))
                    for i in range(len(p1)):
                        dp[i] += t.p0[i] - p1[i]
                    calcdp = np.sum(dp)
                    calcdp = calcdp/len(dp)
                    temp = t.kal.predict(calcdp) #individually call the kalman filters for each trackedobjects
                    t.pos = temp[0:2]
                    t.size = temp[3:5]
                    t.p0 = p1  
            self.pimage = image                
