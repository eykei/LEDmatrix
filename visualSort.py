from samplebase import SampleBase
import time, random

# sudo python3 visualSort.py --led-mapper="U-mapper" --led-chain=4

MATRIXLENGTH=64
#ACTIVE=(255,255,255)
#INACTIVE=(255,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

class DataPoint():
    def __init__(self, value, position): #add color
        self.value=value
        self.position=position
        #self.color=color

class App(SampleBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        self.canvas = self.matrix.CreateFrameCanvas()
        while True:
            self.initializeDataPoints()
            while True:
                if self.isSorted():
                    time.sleep(5)
                    break
                else:
                    self.bubbleSort()
                    self.initializeDataPoints()
                    self.selectionSort()
                    #self.insertionSort()

                

    def draw(self, color):
        '''
        draw each point in datapoint list (dpList)
        '''
        self.canvas.Clear()
        for dp in self.dpList:
            for y in range(dp.value):
                self.canvas.SetPixel(dp.position, 62-y, color[0],color[1],color[2]) #dp.color
        self.matrix.SwapOnVSync(self.canvas)


    def initializeDataPoints(self):
        self.dpList=[]
        values = [x for x in range(MATRIXLENGTH)]
        for p in range(MATRIXLENGTH):
            v = random.choice(values)
            values.remove(v)
            self.dpList.append(DataPoint(v, p))
        self.draw(WHITE)
        time.sleep(3)
        #self.dpList.sort(key = lambda x: x.position)

    def isSorted(self):
        for i in range(MATRIXLENGTH-1):
            if self.dpList[i].value > self.dpList[i+1].value:
                return False
        return True

    def bubbleSort(self):
        n = len(self.dpList)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                self.draw(RED)
                time.sleep(0.1)
                if self.dpList[i].value > self.dpList[i+1].value:
                    self.dpList[i].value, self.dpList[i+1].value = self.dpList[i+1].value, self.dpList[i].value

        time.sleep(5)
                
    def selectionSort(self):
        for i in range(len(self.dpList)):
            min_index = i
            for j in range(i+1, len(self.dpList)):
                self.draw(RED)
                time.sleep(0.1)
                if self.dpList[min_index].value > self.dpList[j].value:
                    min_index = j
            self.dpList[i].value, self.dpList[min_index] = self.dpList[min_index], self.dpList[i].value
        time.sleep(5)

if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()

