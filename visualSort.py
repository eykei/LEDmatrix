from samplebase import SampleBase
import time, random
import algorithms

# sudo python3 visualSort.py --led-pixel-mapper="U-mapper" --led-chain=4

MATRIXLENGTH = 64
#ACTIVE=(255,255,255)
#INACTIVE=(255,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

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
            self.dpList = self.initializeDataPoints()
            self.isSorted(self.dpList)
            self.dpList = algorithms.bubbleSort(self.dpList)
            self.isSorted(self.dpList)

            self.initializeDataPoints()
            self.isSorted(self.dpList)
            self.dpList = algorithms.selectionSort(self.dpList)
            self.isSorted(self.dpList)

            self.initializeDataPoints()
            self.isSorted(self.dpList)
            self.dpList = algorithms.insertionSort(self.dpList)
            self.initializeDataPoints()
            self.isSorted(self.dpList)


    def initializeDataPoints(self):
        datapoints = []
        values = [x for x in range(MATRIXLENGTH)]  # create distinct values for each column
        for position in range(MATRIXLENGTH):
            value = random.choice(values)
            values.remove(value)
            datapoints.append(DataPoint(value, position))
        self.draw(datapoints, WHITE)
        time.sleep(2)
        return datapoints
        #self.dpList.sort(key = lambda x: x.position)

    def draw(self, arr, color):
        '''
        draw each point in datapoint list (dpList)
        arr is a list of datapoint instances
        color is a tuple with 3 values (R, G, B) 0-255
        '''
        self.canvas.Clear()
        for datapoint in arr:
            for y in range(datapoint.value):
                self.canvas.SetPixel(datapoint.position, 62-y, color[0],color[1],color[2])
        self.matrix.SwapOnVSync(self.canvas)

    def isSorted(self, arr):
        for i in range(MATRIXLENGTH-1):
            if self.dpList[i].value > self.dpList[i+1].value:
                self.draw(arr, YELLOW)
                time.sleep(1)
                return False
        self.draw(arr, GREEN)
        time.sleep(1)
        return True


if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()