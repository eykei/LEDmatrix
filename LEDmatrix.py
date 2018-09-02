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

    def draw(self, datapoint):
        for y in range(datapoint.value):
            self.canvas.SetPixel(datapoint.position, y, 255,255,255)


    def initializeDataPoints(self):
        self.dpList=[]
        positions = [x for x in range(MATRIXLENGTH)]
        p = positions.pop(random.choice([positions]))
        for v in range(MATRIXLENGTH):
            self.dpList.append(DataPoint(v,p))




