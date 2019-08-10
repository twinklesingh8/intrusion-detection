import cv2
from pushbullet import PushBullet
import win32com.client as wincl
import time
import os

def intruder_pic():#takes intruder pic
 cam=cv2.VideoCapture(0)
 s,im=cam.read()
 #cv2.imshow("Test Picture",im)
 cv2.imwrite("Intruder.bmp",im)
def suspected_message():#intruder suspected message
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("Intruder Suspected")

#my PushBullet API key
api_key ="o.XWzU7triqJY1XtCJHBtR2n4tL7O0jXzf"
pb =PushBullet(api_key)
pushMsg =pb.push_note("PYTHON : ","Found a Connectivity, is this you? if not message 'No' ")

def Image_send():#pushes captured image to Mobile
    with open("Intruder.bmp", "rb") as pic:
        file_data = pb.upload_file(pic, "Intruder.bmp")
    push = pb.push_file(**file_data)
def logOff():#log off PC if Intruder Suspecteds
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def Control():
    while True:
     val =pb.get_pushes()
     action =val[0]['body']
     print(action)
     if action=='No' or 'no':
        suspected_message()
        intruder_pic()
        Image_send()
        time.sleep(15)
        logOff()
     
Control()
