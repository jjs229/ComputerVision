import cv2
import numpy as np

class KalmanFilterX():
    def __init__(self, model_dims, measure_dims, control_dims=0, X0=None, dtype=np.float32):
        
        self.kf = cv2.KalmanFilter(model_dims, measure_dims, control_dims)
        self.control_dims = control_dims
        
        if X0 is None:
            self.X0 = np.zeros(model_dims, dtype=dtype)
        self.X0 = np.array([[x0] for x0 in X0])
        
        self.kf.controlMatrix = None
        self.kf.measurementMatrix = None
        self.kf.measurementNoiseCov = None
        self.kf.processNoiseCov = None
        
        self.controlMatrix = self.kf.controlMatrix
        self.measurementMatrix = self.kf.measurementMatrix
        self.measurementNoiseCov = self.kf.measurementNoiseCov
        self.processNoiseCov = self.kf.measurementNoiseCov
    
    def updateMatrixes( self ):
        if not np.array_equal(self.controlMatrix, self.kf.controlMatrix):
            self.kf.controlMatrix = self.controlMatrix
            
        if not np.array_equal(self.measurementMatrix, self.kf.measurementMatrix):
            self.kf.measurementMatrix = self.measurementMatrix
            
        if not np.array_equal(self.measurementNoiseCov, self.kf.measurementNoiseCov):
            self.kf.measurementNoiseCov = self.measurementNoiseCov
            
        if not np.array_equal(self.processNoiseCov, self.kf.processNoiseCov):
            self.kf.processNoiseCov = self.processNoiseCov
    
    def correct(self, matrix): 
        self.updateMatrixes()
        print(type(matrix), ' ', type(self.X0.ravel()))
        print(matrix, ' ', self.X0.ravel())
        print(matrix == self.X0.ravel())
        print(matrix - self.X0.ravel())
        self.kf.correct(matrix - self.X0.ravel())
        
    def predict(self, control=None):
        self.updateMatrixes()

        if control is None:
            if self.control_dims == 0:
                return self.X0 + self.kf.predict()
            else:
                control = np.zeros(self.control_dims, dtype=np.float32)
        
        return self.X0 + self.kf.predict(control)
