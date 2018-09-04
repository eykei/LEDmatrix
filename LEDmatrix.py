from samplebase import SampleBase
import time, random

MATRIXLENGTH=64
#ACTIVE=(255,255,255)
#INACTIVE=(255,0,0)

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
            while True:
                self.canvas.Clear()
                for dp in self.dpList:
                    self.draw(dp)
                self.canvas = self.matrix.SwapOnVSync(self.canvas)
                self.bubbleSortStep()
                if self.isSorted():
                    break
                time.sleep(0.5)

    def draw(self, datapoint):
        for dp in self.dpList:
            for y in range(dp.value):
                self.canvas.SetPixel(dp.position, 62-y, 200,200,200)

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

if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()


