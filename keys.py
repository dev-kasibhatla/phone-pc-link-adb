import threading
import logging
from pynput.keyboard import Key, Listener
import Network as net
import Commands as com

keepRunning = True

MOVE_UP = 'w'
MOVE_LEFT = 'a'
MOVE_RIGHT = 'd'
MOVE_DOWN = 's'
movement = [MOVE_UP,MOVE_LEFT,MOVE_RIGHT,MOVE_DOWN]
held=[]

lockControl = True

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-9s) %(message)s',)

legend = {
    'Key.shift':"run",
    'Key.space':"jump",
    'Key.tab':"bag",
    'z':"prone",
    'c':"crouch",
    '`':"settings",
    'k':"pickitem1",
    'l':"pickitem2",
    'r':"reload",
    'p':"pistol",
    'Key.alt_r':"fpp",
    'g':"drive",
    'h':"getin",
    'f':"opendoor",
    'b':"openbox",
    'm':"openmap",
    'x':"revive",
    '1':"meds",
    '2':"grenade",
    'q':"peekleft",
    'e':"peekright"
}


def init():
    pri("Started keys")
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def pri(m):
    logging.debug(m)

def on_press(key):
    k = str(key).strip('\'')
    #print('{0} pressed'.format(key))
    if movement.count(k) >= 1:
        processMovement(k, True)
    else:
        print(k)
        processKeyTaps(k)

def on_release(key):
    k = str(key).strip('\'')
    #print('{0} released'.format(key))
    if movement.count(k) >= 1:
        processMovement(k,False)
    elif key == Key.esc:
        global keepRunning
        # Stop listener
        keepRunning=False
        return False

def processMovement(key,hold):
    if held.count(key)>0 and hold:
        return
    if hold:
        held.append(key)
    else:
        held.remove(key)
    pri("Processing movement")
    if key == MOVE_UP:
        e(com.getSwipe("move up",hold))
    elif key == MOVE_DOWN:
        e(com.getSwipe("move down",hold))
    elif key == MOVE_LEFT:
        e(com.getSwipe("move left",hold))
    elif key == MOVE_RIGHT:
        e(com.getSwipe("move right",hold))

def processKeyTaps(key):
    if key in legend:
        dot(legend[key])


def dot(s):
    e(com.getTap(s))

def e(finalEvent):
    if len(net.clients)>0 and lockControl:
        net.commands.insert(0,finalEvent)
    print(finalEvent)

t3 = threading.Thread(name="keyboardthread",target=init)
t3.start()
