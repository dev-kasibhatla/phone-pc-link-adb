from pynput import mouse
from pynput.mouse import Controller
import Commands as com
import DataManager as data
import Network as net
import threading
import logging
import keys
import time

scale=1.5
mouseRefresh = 0.001 #50 ms

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-9s) %(message)s',)

lockControl = True

button_left = "Button.left"
button_right = "Button.right"
button_middle = "Button.middle"
button_front = "Button.button9"
button_back = "Button.button8"

mow = Controller()
centreX = 1736
centreY = 375
currLoc = (centreX,centreY)

def on_move(x, y):
    global currLoc
    #print('Pointer moved to {0}'.format((x, y)))
    currLoc = (x,y)
    #processMovement(x,y)

def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    #pri(button)
    if pressed:
        if processClick(str(button)):
            return
    if not pressed:
        if not keys.keepRunning:
            net.keepRunning=False
            pri("Stopping")
            return False
        # Stop listener
        return True

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    

look_start = data.Tap("a",1470,622) 
lis=[]
def init():
    pri("Starting control")
    global lis
    global look_start
    for tap in data.taps:
        if tap.name == "lookstart":
            look_start=tap
            pri("lookstart initialized")
    pri("Lookstart not found")
    mow.position = (centreX,centreY)
    with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
        lis.append(listener)
        pri("appended")
        listener.join()
    net.keepRunning=False
    pri("init complete")


def processClick(but):
    global lockControl
    if but == button_left:
        #pri("Left click")
        e(com.getTap("shoot"))
    elif but==button_right:
        #pri("Right click")
        e(com.getTap("scope"))
    elif but==button_middle:
        lockControl= not lockControl
        keys.lockControl=lockControl
        #pri("Middle click")
    elif but==button_front:
        e(com.getTap("gun1"))
    elif but==button_back:
        e(com.getTap("gun2"))


#time based movement calculator

def processMovement():
    while keys.keepRunning:
        if lockControl:    
            #sleep
            mow.position = (centreX,centreY)
            time.sleep(mouseRefresh)
            #pri("Slept")
            #send a swipe
            x,y = currLoc
            dx = int((x - centreX)*scale)
            dy = int((y - centreY)*scale)
            #print('dx= ',dx,'dy= ',dy)
            if abs(dx)>0 and abs(dy)>0:
                e(com.customSwipe(look_start.x,look_start.y,look_start.x+dx,look_start.y-dy))
    t3._stop()

def pri(m):
    logging.debug(m)

def e(finalEvent):
    if len(net.clients)>0 and lockControl:
        net.commands.insert(0,finalEvent)
    else:
        print(finalEvent)

t2 = threading.Thread(name="controlthread",target=init)
t2.start()

t3 = threading.Thread(name="mousethread",target=processMovement)
t3.start()