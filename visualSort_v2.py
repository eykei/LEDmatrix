from samplebase import SampleBase
import time, random, itertools

# sudo python3 visualSort.py --led-pixel-mapper="U-mapper" --led-chain=4

MATRIXLENGTH = 64
#ACTIVE=(255,255,255)
#INACTIVE=(255,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)


class App(SampleBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        # algorithms = [self.bubbleSort, self.selectionSort, self.insertionSort]
        algorithms = [self.bubbleSort]
        algorithms_cycle = itertools.cycle(algorithms)
        self.canvas = self.matrix.CreateFrameCanvas()

        for algorithm in algorithms_cycle:
            array = self.initializeDataPoints()
            # self.isSorted(self.dpList)
            algorithm(array)
            for i in range(MATRIXLENGTH):
                print(array)
            # self.isSorted(self.dpList)


    def initializeDataPoints(self):
        array = random.sample(range(MATRIXLENGTH), MATRIXLENGTH)
        for i in range(len(array)):
            self.draw(i, array[i], RED)
        time.sleep(2)
        return array


    def draw(self, position, value, color):
        for y in range(MATRIXLENGTH):
            self.canvas.SetPixel(position, 62 - y, 0, 0, 0)
        for y in range(value):
            self.canvas.SetPixel(position, 62 - y, color[0], color[1], color[2])
        self.matrix.SwapOnVSync(self.canvas)

    # def isSorted(self, arr):
    #     for i in range(MATRIXLENGTH-1):
    #         if self.dpList[i].value > self.dpList[i+1].value:
    #             self.draw(arr, YELLOW)
    #             time.sleep(1)
    #             return False
    #     self.draw(arr, GREEN)
    #     time.sleep(1)
    #     return True


    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.draw(j+1, arr[j+1], WHITE)
                    self.draw(j, arr[j], WHITE)
                    time.sleep(0.05)
                    self.draw(j+1, arr[j+1], RED)
                    self.draw(j, arr[j], RED)


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
                    i += 1
                else:
                    arr[k].value = R[j].value
                    j += 1
                k += 1

            while i < len(L):
                arr[k].value = L[i].value
                i += 1
                k += 1

            while j < len(R):
                arr[k].value = R[j].value
                j += 1
                k += 1

            self.draw(arr, RED)
            time.sleep(0.05)





if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()