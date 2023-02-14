from player import Player
from detector import Detector
#from colordetector import ColorDetector
from motiondetector import MotionDetector
from tracker import Tracker
import threading
from manualdetector import ManualDetector
import cv2
import time


#detector.run should get no parameters. init img as None, newdet = False, running = true. If self.image is not none, then do the running
    #also put a while ruuning == true loop in run function so it loops. Add img = self.img, self.img = None to reset to go back to sleep
    #newdet == true
    #time.sleep(0.2s) this is adjusted for frame rate
    #add function def set(img): than sets self.img to img parameter
    #add def get(self): if newdet ==false, newdet=False, return true, detections | return false, []
#then get rid of detector.run here in main.py
#add detector.set and detector.draw
#n, d = detector.get()
#if n: tracker.set(d)
#tracker.track()
#detector.draw, tacker.draw
#if condition from detector then execute add tracker.set tracker.track to this main function
#def close(self): self.running == false


player = Player()
#detector =Detector()
#detector =ColorDetector()
#detector = MotionDetector()
mandetector = ManualDetector()
tracker = Tracker()

#detectorThread = Thread(detector.run)

while True:
    ret,img = player.run()
    if not ret:
        break
    mandetector.set(img)
    #detector.set(img)
    #detector.start()
    n, d = mandetector.get()
    #n, d = detector.get()
    if n:
        tracker.set(d)
    #tracker.track(img)
    #mandetector.draw(img)
    #detector.draw(img)
    #if n:
    tracker.draw(img)
    key=player.draw(img)
    if key == ord('q') or key==27:
        break
player.close()
tracker.close()
mandetector.close()
#detectorThread.join()
    
