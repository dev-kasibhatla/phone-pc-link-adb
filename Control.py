from pynput import mouse
import Commands as com
import DataManager as data
import AdbManager as adb

button_left = "Button.left"
button_right = "Button.right"
button_middle = "Button.middle"
button_front = "Button.button9"
button_back = "Button.button8"

def on_move(x, y):
    # print('Pointer moved to {0}'.format(
    #     (x, y)))
    processMovement(x,y)

def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    #print(button)
    if pressed:
        if processClick(str(button)):
            return
    if not pressed:
        # Stop listener
        return True

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    

look_start = data.Tap("a",0,0) 
lis=[]
def init():
    global lis
    global look_start
    for tap in data.taps:
        if tap.name == "lookstart":
            look_start=tap
            print("lookstart initialized")
    with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
        lis.append(listener)
        print("appended")
        listener.join()


def processClick(but):
    if but == button_left:
        print("Left click")
    elif but==button_right:
        print("Right click")
    elif but==button_middle:
        print("Middle click")
    elif but==button_front:
        print("Front click")
    elif but==button_back:
        print("Back click")

px=0
py=0
dx=0
dy=0
threshold=120
scale=0.5
look_duration = 50

def processMovement(x,y):
    global px
    global py
    global dx
    global dy
    dx += x-px
    dy += y-py
    px=x
    py=y
    if abs(dx)>threshold or abs(dy)>threshold:
        #now move that much
        print("dx",dx,"dy",dy)
        adb.e(com.customSwipe(look_start.x,look_start.y,look_start.x+dx,look_start.y+dy,look_duration))
        dx=0
        dy=0

