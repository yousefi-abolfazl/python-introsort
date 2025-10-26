

THRESHOLD = 16

def insertion_sort(array, low, high):
    pass

def heapify(array, n, i):
    largest = i

    l = 2 * i + 1

    r = 2 * i + 2

    if l < n and array[l] > array[n]:
        largest = l
    if r < n and array[r] > array[n]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
    
def heapsort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]

        heapify(array, i, 0)

def quickSort(array, low, high):
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

def partition(array, low, high):
    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def introsort(array, low, high, maxdepth):
    length = high - low

    if length <= THRESHOLD:
        insertion_sort(array, low, high)
        return
    
    if maxdepth == 0:
        heapsort(array, low, high)
        return

