import cv2
import numpy as np
import pyfirmata
import time

class ServoController(object):
    theta0 = 90.0; 
    theta1 = 90.0;
    theta2 = 90.0;
    theta3 = 0.0;
 
    board = None
    servo0 = None
    servo1 = None
    servo2 = None
    servo3 = None
    servo4 = None


    def __init__(self):
        print("in __init__")
        self.board = pyfirmata.ArduinoMega('COM7')
    
    #    self.board.servo_config(3, angle = self.theta0)
    #    self.servo0 = self.board.get_pin('d:3:s')
    #    self.servo0.write(self.theta0)
        #joint 4
        self.board.servo_config(8, angle = 0)
        self.servo4 = self.board.get_pin('d:8:s')
        self.servo4.write(0)

    #    #joint 1
    #    self.board.servo_config(11, angle = 0)
    #    self.servo1 = self.board.get_pin('d:11:s')
    #    self.servo1.write(0)

        #joint 3
    #    self.board.servo_config(9, angle = 0)
    #    self.servo3 = self.board.get_pin('d:9:s')
    #    self.servo3.write(0)

        #joint 2
    #   self.board.servo_config(10, angle = 0)
    #    self.servo2 = self.board.get_pin('d:10:s')
    #    self.servo2.write(0)

    def __del__(self):
        print("in __del__")
        self.goto(90, 90 ,90)
        self.board.exit()

    def wave(self):
        self.servo4.write(0)
        for j in range(5):
            for x in range (0,61):
                self.servo4.write(x)
                time.sleep(0.005)
            for x in range (59,0,-1):
                self.servo4.write(x)
                time.sleep(0.005)
    
    #def move2And3(self):
    #    self.servo2.write(90.1)
    #    time.sleep(0.05)
    #    self.servo2.write(89.9)
    #    time.sleep(0.05)
    #    self.servo3.write(90.1)
    #    time.sleep(0.08)
    #    self.servo3.write(89.9)

    #def baseSpin(self):
    #    for j in range(2):
    #        self.servo1.write(90.1)
    #        time.sleep(0.5)
    #    for x in range(2):
    #        self.servo1.write(89.9)
    #        time.sleep(0.5)
            #self.servo1.write(90)

    def moveObjD(self):

        cap = cv2.VideoCapture(0)

        cap.set(3, 480)
        cap.set(4, 320)

        _, frame = cap.read()
        rows, cols, _ = frame.shape

        x_medium = int(cols / 2)
        y_medium = int(rows / 2)
        center = int(cols / 2)
        position = 90 # degrees
        while True:
            _, frame = cap.read()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            # red color
            low_red = np.array([161, 155, 84])
            high_red = np.array([179, 255, 255])
            red_mask = cv2.inRange(hsv_frame, low_red, high_red)
            contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
            
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                
                x_medium = int((x + x + w) / 2)
                break
            
            cv2.line(frame, (x_medium, y_medium), (x_medium, y_medium), (0, 255, 0), 2)
            #cv2.line(frame, (y_medium, 0), (y_medium, 480), (0, 255, 0), 2)
            
            cv2.imshow("Frame", frame)
            
            
            key = cv2.waitKey(5)
            
            if key == 27:
                break
            
            # Move servo motor
            if x_medium < center -30 and position<=180:
                position += 0.05
            elif x_medium > center + 30 and position>=0:
                position -= 0.05
            else:
                position = position
                
            print(round(position))
            self.servo1.write(position)
            
        cap.release()
        cv2.destroyAllWindows()

    def set0(self, theta0_desired):
        theta0_desired = max(theta0_desired, 0.0)
        theta0_desired = min(theta0_desired, 180.0)
        while abs(self.theta0-theta0_desired)>0.1:
            if self.theta0 <= theta0_desired:
                self.theta0 = self.theta0 + 1.0
            elif self.theta0 > theta0_desired:
                self.theta0 = self.theta0 - 1.0

            self.servo0.write(self.theta0)
            time.sleep(0.015)
        print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2))

    def set1(self, theta1_desired):
        theta1_desired = max(theta1_desired, 0.0)
        theta1_desired = min(theta1_desired, 180.0)
        while abs(self.theta1-theta1_desired)>0.1:
            if self.theta1 <= theta1_desired:
                self.theta1 = self.theta1 + 1.0
            elif self.theta1 > theta1_desired:
                self.theta1 = self.theta1 - 1.0

            self.servo1.write(self.theta1)
            time.sleep(0.015)
        print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2))

        
    def set2(self, theta2_desired):
        theta2_desired = max(theta2_desired, 0.0)
        theta2_desired = min(theta2_desired, 180.0)
        while abs(self.theta2-theta2_desired)>0.1:
            if self.theta2 <= theta2_desired:
                self.theta2 = self.theta2 + 1.0
            elif self.theta2 > theta2_desired:
                self.theta2 = self.theta2 - 1.0

            self.servo2.write(self.theta2)
            time.sleep(0.015)
        print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2))

    def set3(self, theta3_desired):
        theta3_desired = max(theta3_desired, 0.0)
        theta3_desired = min(theta3_desired, 90.0)
        while abs(self.theta3-theta3_desired)>0.1:
            if self.theta3 <= theta3_desired:
                self.theta3 = self.theta3 + 1.0
            elif self.theta3 > theta3_desired:
                self.theta3 = self.theta3 - 1.0

            self.servo3.write(self.theta3)
            time.sleep(0.015)
            
    def goto(self, theta0_desired, theta1_desired, theta2_desired):
        self.set0(theta0_desired)
        self.set1(theta1_desired)
        self.set2(theta2_desired)

        print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2))
        time.sleep(0.2)
  


