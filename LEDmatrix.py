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
        self.initializeDataPoints()

        while True:
            for dp in self.dpList:
                self.draw(dp)
            self.matrix.SwapOnVSync(self.canvas)
            dpList = self.bubbleSortStep(self.dpList)
            time.sleep(1)

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

    def bubbleSortStep(self,dpList):
        for i in range(len(dpList)-1):
            if dpList[i].value > dpList[i+1].value:
                dpList[i], dpList[i+1] = dpList[i+1], dpList[i]
        return dpList




if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()


