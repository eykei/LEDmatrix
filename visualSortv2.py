'''
description: Displays various sorting algorithms in action on the LED matrix

usage: on the Raspberry Pi, navigate to visualSort.py
>sudo python3 visualSort.py --led-pixel-mapper="U-mapper" --led-chain=4

status: Working

todo:
'''

from samplebase import SampleBase
import time, random, itertools



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
        algorithms = [self.bubbleSort, self.insertionSort, self.selectionSort, self.mergeSort] # no parenthesis after name
        algorithms_cycle = itertools.cycle(algorithms)
        self.canvas = self.matrix.CreateFrameCanvas()

        for algorithm in algorithms_cycle:
            array = self.initializeDataPoints()
            self.isSorted(array)
            algorithm(array)
            self.isSorted(array)


    def initializeDataPoints(self):
        array = random.sample(range(1, MATRIXLENGTH+1), MATRIXLENGTH)
        for i in range(len(array)):
            self.draw(i, array[i], RED)
        time.sleep(2)
        return array


    def draw(self, position, value, color):
        for y in range(MATRIXLENGTH):
            self.canvas.SetPixel(position, 63 - y, 0, 0, 0)
        for y in range(value):
            self.canvas.SetPixel(position, 63 - y, color[0], color[1], color[2])
        self.matrix.SwapOnVSync(self.canvas)


    def isSorted(self, arr):
        for i in range(MATRIXLENGTH-1):
            if arr[i] < arr[i+1]:
                self.draw(i, arr[i], GREEN)
                self.draw(i+1, arr[i+1], GREEN)
            else:
                for j in range(MATRIXLENGTH):
                    self.draw(j, arr[j], RED)
                time.sleep(1)
                return False
        time.sleep(3)
        return True


    def bubbleSort(self, arr):
        # "bubble" highest values to the top
        print("Bubble Sort")
        n = len(arr)
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.draw(j+1, arr[j+1], WHITE)
                    self.draw(j, arr[j], WHITE)
                    time.sleep(0.01)
                    self.draw(j+1, arr[j+1], RED)
                    self.draw(j, arr[j], RED)


    def selectionSort(self, arr):
        # find the minimum element of the unsorted part of the array and put it into the sorted part of the array
        print("Selection Sort")
        n = len(arr)
        for i in range(0, n):
            min_index = i
            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            self.draw(i, arr[i], WHITE)
            self.draw(min_index, arr[min_index], WHITE)
            time.sleep(0.01)
            self.draw(i, arr[i], RED)
            self.draw(min_index, arr[min_index], RED)


    def insertionSort(self, arr):
        # pull each element and insert it into its place, shifting the position of elements after it if necessary
        print("Insertion Sort")
        n = len(arr)
        for i in range(0, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                self.draw(j + 1, arr[j + 1], WHITE)
                time.sleep(0.05)
                self.draw(j + 1, arr[j + 1], RED)
                j -= 1
            arr[j + 1] = key
            self.draw(j+1, arr[j+1], WHITE)
            time.sleep(0.05)
            self.draw(j + 1, arr[j+1], RED)


    def mergeSort(self, arr):
        # break down array in to length 1 arrays, merge them back together recursively
        print("Merge Sort")
        n = len(arr)
        if n > 1:
            M = n // 2
            L = arr[:M]
            R = arr[M:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    self.draw(k, arr[k], WHITE)
                    time.sleep(0.05)
                    self.draw(k, arr[k], RED)
                    i += 1
                else:
                    arr[k] = R[j]
                    self.draw(j, arr[j], WHITE)
                    time.sleep(0.05)
                    self.draw(k, arr[k], RED)
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                self.draw(k, arr[k], WHITE)
                time.sleep(0.05)
                self.draw(k, arr[k], RED)
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                self.draw(k, arr[k], WHITE)
                time.sleep(0.05)
                self.draw(k, arr[k], RED)
                j += 1
                k += 1


if __name__ == "__main__":
    app = App()
    if (not app.process()):
        app.print_help()