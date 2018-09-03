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
                prev_dpList=self.dpList
                self.canvas.Clear()
                for dp in self.dpList:
                    self.draw(dp)
                self.canvas = self.matrix.SwapOnVSync(self.canvas)
                self.bubbleSortStep()
                if self.dpList == prev_dpList:
                    break
                time.sleep(0.5)

    def draw(self, datapoint):
        for y in range(1, datapoint.value+1):
            self.canvas.SetPixel(datapoint.position, 63-y, 200,200,200)

    def initializeDataPoints(self):
        self.dpList=[]
        positions = [x for x in range(MATRIXLENGTH)]
        
        for v in range(MATRIXLENGTH):
            p = random.choice(positions)
            positions.remove(p)
            self.dpList.append(DataPoint(v,p))
        
        for x in range(len(self.dpList)):
            print(self.dpList[x].value, self.dpList[x].position)
        self.dpList.sort(key = lambda x: x.position)
        for x in range(len(self.dpList)):
            print(self.dpList[x].value, self.dpList[x].position)
        input()

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


