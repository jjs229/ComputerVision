# ComputerVision
This Repository servers as a base for future computer vision projects. It is not a complete work, nor a beautiful collection of libraries, but rather an eclectic assemblance of classes used together for prototyping results and testing hardware.

main2.py is the main file and is constantly adjusted depending on the project.

To do list:
- Add option for second camera and incorporate homography capabilities
- Add 3D to all trackedObjects objects
- Add additional attributes to trackedObjects
- Add AI/Tensorflow for object detection
- Remultithread everything

Current Files:

- Player
  + Used to choose video input, pausing, framerate, and output
  + Can use more user friendly features for testing
- Detector
  + Parent Detector Class
- Color Detector
  + Can currently detect one color. Should add functions to easily detect any color input
  + Color detectors are not super useful
- Motion Detector
  + Detects any motion. Not direction
  + Blurs and thresholds to map movement as objects
  + Should be recalibrated with different cameras
- Manual Tracker
  + Is used so any used can select/highlight something in the image
- TrackedObjects
  + Carries all characteristics for any tracked objects
  + Times for on and off screen and when to disappear
  + Coordinates
- Tracker
  + Uses LK algorithm to predict the movement of any objects while waiting for detector to reconfirm position of object
  + Fast paced
  + Complex
- KalmanFilterX
  + Basically the normal KalmanFilter class, except with easier x intialization
