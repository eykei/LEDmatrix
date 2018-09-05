from samplebase import SampleBase
import time, random

# sudo python3 LEDmatrix.py --led-mapper="U-mapper" --led-chain=4

MATRIXLENGTH=64
#ACTIVE=(255,255,255)
#INACTIVE=(255,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

class DataPoint():
    def __init__(self, value, position):
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
            self.draw(WHITE)
            time.sleep(3)
            while True:
                self.draw(RED)
                if self.isSorted():
                    time.sleep(5)
                    break
                else:
                    self.bubbleSortStep()
                    #self.selectionSortStep()
                time.sleep(0.1)
                

    def draw(self, color):
        self.canvas.Clear()
        for dp in self.dpList:
            for y in range(dp.value):
                self.canvas.SetPixel(dp.position, 62-y, color[0],color[1],color[2])
        self.matrix.SwapOnVSync(self.canvas)

    def initializeDataPoints(self):
        self.dpList=[]
        val = [x for x in range(MATRIXLENGTH)]
        for p in range(MATRIXLENGTH):
            v = random.choice(val)
            val.remove(v)
            self.dpList.append(DataPoint(v,p))

        #self.dpList.sort(key = lambda x: x.position)

    def isSorted(self):
        for i in range(MATRIXLENGTH-1):
            if self.dpList[i].value > self.dpList[i+1].value:
                return False
        return True

    def bubbleSortStep(self):
        n = 1
        for i in range(MATRIXLENGTH-n):
            n+=1
            if self.dpList[i].value > self.dpList[i+1].value:
                self.dpList[i].value, self.dpList[i+1].value = self.dpList[i+1].value, self.dpList[i].value
                
    def selectionSortStep(self):
        min_index = 0
        for i in range(MATRIXLENGTH):
            min = self.dpList[min_index].value
            if self.dpList[i].value < min:
                self.dpList[i].value, self.dpList[min_index].value = self.dpList[min_index].value, self.dpList[i].value
                min_index += 1

if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()


