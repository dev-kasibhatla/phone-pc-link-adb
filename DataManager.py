tapFileLocation = "tap.txt"
swipeFileLocation = "swipe.txt"
swipes=[]
taps=[]

class DM:
    def getTapData(self):
        tapFile = open(tapFileLocation,'rt')
        lines = tapFile.read().splitlines()
        rem=[]
        for line in lines :
            if line[0] == '#':
                rem.append(line)
        for l in rem:
            lines.remove(l)
        for line in lines:
            #print("Exploding "+line)
            contents = line.split(',')
            t = Tap(contents[0],contents[1],contents[2])
            taps.append(t)
        
        print("Taps collected: "+str(len(taps)))

    def getSwipeData(self):
        swipeFile = open(swipeFileLocation,'rt')
        lines = swipeFile.read().splitlines()
        rem=[]
        for line in lines :
            if line[0] == '#':
                rem.append(line)
        for l in rem:
            lines.remove(l)
        for line in lines:
            print("Exploding "+line)
            contents = line.split(',')
            t = Swipe(contents[0],contents[1],contents[2], contents[3],contents[4])
            swipes.append(t)
        
        print("Swipes collected: "+str(len(taps)))


class Tap:
    def __init__(self, name,x,y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        #print(name+' '+x+' '+y)

class Swipe:
    def __init__(self, name,x1,y1,x2,y2):
        self.name = name
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        #print(name+' '+x1+' '+y1+' '+x2+' '+y2)
