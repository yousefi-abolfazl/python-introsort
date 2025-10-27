import math

def introsort(array, low, high, depthlimit=None):
    length = high - low + 1

    if length <= 1:
        return
    
    THRESHOLD = 16
    if depthlimit is None:
        depthlimit = 2 * int(math.log2(length))

    if length <= THRESHOLD:
        insertionSort(array, low, high)
    
    elif depthlimit == 0:
        heapSort(array, low, high)
        
    else:
        if low >= high:
            return
        pi = partition(array, low, high)
        introsort(array, low, pi - 1, depthlimit - 1)
        introsort(array, pi + 1, high, depthlimit - 1)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def insertionSort(array, low, high):
    for j in range(low + 1, high + 1):
        key = array[j]
        i = j - 1
        while i >= low and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key


def heapify(array, low, high, i):
    largest = i
    l = 2 * (i - low) + 1 + low
    r = 2 * (i - low) + 2 + low
    if l <= high and array[l] > array[largest]:
        largest = l
    if r <= high and array[r] > array[largest]:
        largest = r

    if largest != i:
        swap(array, i, largest)
        heapify(array, low, high, largest)


def heapSort(array, low, high): 
    for i in range(low + (high - low) // 2, low - 1, -1):
        heapify(array, low, high, i)
    
    for i in range(high, low, -1):
        swap(array, low, i)
        heapify(array, low, i - 1, low)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    i += 1
    swap(array, i, high)
    return i

array = [50, 16, 20, 0, 2, 7]

introsort(array, 0,5)

print(array)