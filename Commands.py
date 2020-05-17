import DataManager as D
import json
tapDelay = 25


idCounter = 0
EVENT_TAP=0
EVENT_SWIPE=1
EVENT_MOUSE=2

def init():
    data = D.DM()
    data.getTapData()
    data.getSwipeData()
    #print("Complete")

def getTap2(action):
    #search for name and return
    for tap in D.taps:
        if tap.name == action:
            return "swipe "+str(tap.x)+' '+str(tap.y)+ ' ' + str(tap.x)+' '+str(tap.y) + ' ' + str(tapDelay)
    print("Can't find "+action)

def getSwipe2(action):
    for swipe in D.swipes:
        if swipe.name == action:
            return "swipe "+str(swipe.x1)+' '+str(swipe.y1)+ ' ' + str(swipe.x2)+' '+str(swipe.y2) + ' ' + str(tapDelay*2)
    print("Can't find "+action)

def customSwipe2(x1,y1,x2,y2,ms):
    return str("swipe "+str(x1)+' '+str(y1)+ ' ' + str(x2)+' '+str(y2) + ' ' + str(ms))


#new stuff
def getTap(action):
    global idCounter
    #search for name and return
    for tap in D.taps:
        if tap.name == action:
            #make a json object
            jo = {
                "id": idCounter,
                "type": EVENT_TAP,
                "x1":tap.x,
                "x2":tap.x,
                "y1":tap.y,
                "y2":tap.y,
                "hold":False
            }
            idCounter+=1
            return json.dumps(jo)
    print("Can't find "+action)

def getSwipe(action, hold):
    global idCounter
    for swipe in D.swipes:
        if swipe.name == action:
            #make a json object
            jo = {
                "id": idCounter,
                "type": EVENT_SWIPE,
                "x1":swipe.x1,
                "x2":swipe.x2,
                "y1":swipe.y1,
                "y2":swipe.y2,
                "hold":hold
            }
            idCounter+=1
            return json.dumps(jo)
    print("Can't find "+action)

def customSwipe(x1,y1,x2,y2):
    global idCounter
    jo = {
        "id": idCounter,
        "type": EVENT_MOUSE,
        "x1":x1,
        "x2":x2,
        "y1":y1,
        "y2":y2,
        "hold":False
    }
    idCounter+=1
    return json.dumps(jo)