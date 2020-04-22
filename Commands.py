import DataManager as D
tapDelay = 50
def init():
    data = D.DM()
    data.getTapData()
    data.getSwipeData()
    #print("Complete")

def getTap(action):
    #search for name and return
    for tap in D.taps:
        if tap.name == action:
            return "swipe "+str(tap.x)+' '+str(tap.y)+ ' ' + str(tap.x)+' '+str(tap.y) + ' ' + str(tapDelay)
    print("Can't find "+action)

def getSwipe(action):
    for swipe in D.swipes:
        if swipe.name == action:
            return "swipe "+str(swipe.x1)+' '+str(swipe.y1)+ ' ' + str(swipe.x2)+' '+str(swipe.y2) + ' ' + str(tapDelay*2)
    print("Can't find "+action)

def customSwipe(x1,y1,x2,y2,ms):
    return str("swipe "+str(x1)+' '+str(y1)+ ' ' + str(x2)+' '+str(y2) + ' ' + str(ms))