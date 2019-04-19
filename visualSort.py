from samplebase import SampleBase
import time, random
import itertools

# sudo python3 visualSort.py --led-pixel-mapper="U-mapper" --led-chain=4

MATRIXLENGTH = 64
#ACTIVE=(255,255,255)
#INACTIVE=(255,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)

class DataPoint():
    def __init__(self, value, position): #add color
        self.value=value
        self.position=position
        #self.color=color

class App(SampleBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):

        # algorithms = [self.bubbleSort, self.selectionSort, self.insertionSort]
        algorithms = [self.bubbleSort, self.mergeSort]
        algorithms_cycle = itertools.cycle(algorithms)

        self.canvas = self.matrix.CreateFrameCanvas()
        for algorithm in algorithms_cycle:
            self.dpList = self.initializeDataPoints()
            self.isSorted(self.dpList)
            algorithm(self.dpList)
            for i in range(MATRIXLENGTH):
                print(self.dpList[i].value)
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
        # self.canvas.Clear()
        for datapoint in arr:
            for y in range(MATRIXLENGTH):
                self.canvas.SetPixel(datapoint.position, 62 - y, 0, 0, 0)
            for y in range(datapoint.value):
                self.canvas.SetPixel(datapoint.position, 62 - y, color[0],color[1],color[2])
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


    def bubbleSort(self, arr):
        tic = time.clock()
        n = len(arr)
        for i in range(0, n):
            self.draw(arr, RED)
            time.sleep(0.05)
            for j in range(0, n - i - 1):

                if arr[j].value > arr[j + 1].value:
                    arr[j].value, arr[j + 1].value = arr[j + 1].value, arr[j].value
        toc = time.clock()
        print("Bubble Sort time: ", end="")
        print(toc - tic)


    def selectionSort(self, arr):
        tic = time.clock()
        n = len(arr)
        for i in range(0, n):
            min_index = i
            self.draw(arr, RED)
            time.sleep(0.05)
            for j in range(i + 1, n):
                if arr[min_index].value > arr[j].value:
                    min_index = j
            arr[i].value, arr[min_index].value = arr[min_index].value, arr[i].value
        toc = time.clock()
        print("Selection Sort time: ", end="")
        print(toc - tic)


    def insertionSort(self, arr):
        tic = time.clock()
        n = len(arr)
        for i in range(0, n):
            self.draw(arr, RED)
            time.sleep(0.05)
            key = arr[i].value
            j = i - 1
            while j >= 0 and key < arr[j].value:
                arr[j + 1].value = arr[j].value
                j -= 1
            arr[j + 1].value = key
        toc = time.clock()
        print("Insertion Sort time: ", end="")
        print(toc - tic)


    def mergeSort(self, arr):



        n = len(arr)
        if n > 1:
            M = n // 2
            L = arr[:M]
            R = arr[M:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i].value < R[j].value:
                    arr[k].value = L[i].value
                    #arr[k].position = L[i].position
                    i += 1
                else:
                    arr[k].value = R[j].value
                    #arr[k].position = R[j].position
                    j += 1
                k += 1

            while i < len(L):
                arr[k].value = L[i].value
                #arr[k].position = L[i].position
                i += 1
                k += 1

            while j < len(R):
                arr[k].value = R[j].value
                #arr[k].position = R[j].position
                j += 1
                k += 1

            self.draw(arr, RED)
            time.sleep(0.05)





if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()