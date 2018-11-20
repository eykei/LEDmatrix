from samplebase import SampleBase
import time, random

# sudo python3 visualSort.py --led-pixel-mapper="U-mapper" --led-chain=4

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
        self.dpList = []

    def run(self):
        self.canvas = self.matrix.CreateFrameCanvas()
        while True:
            self.initializeDataPoints()
            while True:
                if self.isSorted():
                    time.sleep(5)
                    break
                else:
                    self.bubbleSort(self.dpList)
                    self.initializeDataPoints()
                    self.selectionSort(self.dpList)
                    self.initializeDataPoints()
                    self.insertionSort(self.dpList)
                    self.initializeDataPoints()
                    self.mergeSort(self.dpList)
                    self.initializeDataPoints()
                

    def draw(self, arr, color):
        '''
        draw each point in datapoint list (dpList)
        '''
        self.canvas.Clear()
        for dp in arr:
            for y in range(dp.value):
                self.canvas.SetPixel(dp.position, 62-y, color[0],color[1],color[2]) #dp.color
        self.matrix.SwapOnVSync(self.canvas)


    def initializeDataPoints(self):
        values = [x for x in range(MATRIXLENGTH)]
        for p in range(MATRIXLENGTH):
            v = random.choice(values)
            values.remove(v)
            self.dpList.append(DataPoint(v, p))
        self.draw(self.dpList, WHITE)
        time.sleep(3)
        #self.dpList.sort(key = lambda x: x.position)

    def isSorted(self):
        for i in range(MATRIXLENGTH-1):
            if self.dpList[i].value > self.dpList[i+1].value:
                return False
        return True

    def bubbleSort(self, arr):
        tic = time.clock()
        n = len(arr)
        for i in range(0, n):
            self.draw(arr, RED)
            time.sleep(0.1)
            for j in range(0, n-i-1):

                if arr[j].value > arr[j+1].value:
                    arr[j].value, arr[j+1].value = arr[j+1].value, arr[j].value
        toc = time.clock()
        print("Bubble Sort time: ", end="")
        print(toc - tic)
        if self.isSorted():
            self.draw(arr, GREEN)
            time.sleep(5)
        else:
            self.draw(arr, YELLOW)

                
    def selectionSort(self, arr):
        tic = time.clock()
        n = len(arr)
        for i in range(0, n):
            min_index = i
            self.draw(arr, RED)
            time.sleep(0.1)
            for j in range(i+1, n):
                if arr[min_index].value > arr[j].value:
                    min_index = j
            arr[i].value, arr[min_index].value = arr[min_index].value, arr[i].value
        toc = time.clock()
        print("Selection Sort time: ", end="")
        print(toc-tic)
        if self.isSorted():
            self.draw(arr, GREEN)
            time.sleep(5)
        else:
            self.draw(arr, YELLOW)


    def insertionSort(self, arr):
        tic = time.clock()
        n = len(arr)
        for i in range(0,n):
            self.draw(arr, RED)
            time.sleep(0.1)
            key = arr[i].value
            j = i-1
            while j >= 0 and key < arr[j].value:
                arr[j+1].value = arr[j].value
                j -= 1
            arr[j+1].value = key
        toc = time.clock()
        print("Insertion Sort time: ", end="")
        print(toc-tic)
        if self.isSorted():
            self.draw(arr, GREEN)
            time.sleep(5)
        else:
            self.draw(arr, YELLOW)


    def mergeSort(self, arr):
        n = len(arr)
        if n > 1:
            M = n//2
            L = arr[:M]
            R = arr[M:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                self.draw(arr, RED)
                time.sleep(0.1)
                if L[i] < R[j]:
                    arr[k].value = L[i]
                    i += 1
                else:
                    arr[k].value = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k].value = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k].value = R[i]
                j += 1
                k += 1
        if self.isSorted():
            self.draw(arr, GREEN)
            time.sleep(5)
        else:
            self.draw(arr, YELLOW)


if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()