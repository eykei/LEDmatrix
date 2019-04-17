import time

MATRIXLENGTH = 64
#ACTIVE=(255,255,255)
#INACTIVE=(255,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

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
    return arr
    if self.isSorted():
        self.draw(arr, GREEN)
        time.sleep(1)
    else:
        self.draw(arr, YELLOW)


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
    return arr



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
    return arr
    if self.isSorted():
        self.draw(arr, GREEN)
        time.sleep(1)
    else:
        self.draw(arr, YELLOW)


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
                arr[k].position = L[i].position
                i += 1
            else:
                arr[k].value = R[j].value
                arr[k].position = R[j].position
                j += 1
            k += 1

        while i < len(L):
            arr[k].value = L[i].value
            arr[k].position = L[i].position
            i += 1
            k += 1

        while j < len(R):
            arr[k].value = R[j].value
            arr[k].position = R[j].position
            j += 1
            k += 1

        self.draw(arr, RED)
        time.sleep(0.1)