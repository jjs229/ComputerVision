from kalmanfilterx import KalmanFilterX
import numpy as np
import time


class trackedObject():
    type = None
    pos = None
    size = None
    tin = 0
    tout = 0
    p0 = 0
    newdet = False

    def __init__(self, d):
        self.pos = d[0]
        self.size = d[1]
        self.tin = time.time()
        #initializing Kalman filter with initialization of class
        self.kal = KalmanFilterX(6, 6, 6, d) #6,6,6,[0,0,0,0,0,0,0]
        # #Fh = img.width
        # #Fw = img.height
        # #Ep = (self.kp * sqrt(Fh**2 + Fw**2)) #find a place to get frame width and height
        Ep = 0.03 #stole this from someone else's code
        self.kal.processNoiseCov= Ep*np.identity(6)
        self.kal.measurementNoiseCov = 0.1 #Can probably set this to 0 because it will be so low
        self.kal.measurementMatrix = np.identity(6) #measurement matrix???
        self.kal.controlMatrix = np.array([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
        
        #def initKF(self, img): 
        #     #X(k+1) AYk +Buk+1 +QXk #A + qxK, model matrix, we don;t know, B is control matrix, u is external input, Q is process noise covariant
        #     #Yk+1=CXk+1 + RXk+1  # C is observability matrix(how many dimensions can we observe), R is measurement noise covariant
        #     #x = [x,y,z,w,h,d]
        #    return