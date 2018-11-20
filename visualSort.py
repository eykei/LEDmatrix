from samplebase import SampleBase
import time, random

# sudo python3 visualSort.py --led-mapper="U-mapper" --led-chain=4

MATRIXLENGTH=64
#ACTIVE=(255,255,255)
#INACTIVE=(255,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
YELLOW=(255,255,0)

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
                    # self.bubbleSort()
                    # self.initializeDataPoints()
                    # self.selectionSort()
                    # self.initializeDataPoints()
                    self.insertionSort()
                    self.initializeDataPoints()

                

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
        tic = time.clock()
        n = len(self.dpList)
        for i in range(0, n):
            self.draw(RED)
            time.sleep(0.1)
            for j in range(0, n-i-1):

                if self.dpList[j].value > self.dpList[j+1].value:
                    self.dpList[j].value, self.dpList[j+1].value = self.dpList[j+1].value, self.dpList[j].value
        toc = time.clock()
        print("Bubble Sort time: ", end="")
        print(toc - tic)
        if self.isSorted():
            self.draw(GREEN)
            time.sleep(5)
        else:
            self.draw(YELLOW)

                
    def selectionSort(self):
        tic = time.clock()
        n = len(self.dpList)
        for i in range(0, n):
            min_index = i
            self.draw(RED)
            time.sleep(0.1)
            for j in range(i+1, n):
                if self.dpList[min_index].value > self.dpList[j].value:
                    min_index = j
            self.dpList[i].value, self.dpList[min_index].value = self.dpList[min_index].value, self.dpList[i].value
        toc = time.clock()
        print("Selection Sort time: ", end="")
        print(toc-tic)
        if self.isSorted():
            self.draw(GREEN)
            time.sleep(5)
        else:
            self.draw(YELLOW)


    def insertionSort(self):
        tic = time.clock()
        n = len(self.dpList)
        for i in range(0,n):
            key = self.dpList[i].value
            j = i-1
            while j >= 0 and key < self.dpList[j].value:
                self.dpList[j+1].value = self.dpList[j].value
                j -= 1
            self.dpList[j+1].value = key
        toc = time.clock()
        print("Insertion Sort time: ", end="")
        print(toc-tic)
        if self.isSorted():
            self.draw(GREEN)
            time.sleep(5)
        else:
            self.draw(YELLOW)

if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()