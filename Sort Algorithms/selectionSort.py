array = [20, 35, -15, 7, 55, 1, -22]
print(array)

def swap(array, largest, lastUnsortedIndex):
    temp = array[largest]
    array[largest] =  array[lastUnsortedIndex]
    array[lastUnsortedIndex] = temp



lastUnsortedIndex = len(array)-1

for i in range(lastUnsortedIndex, 0, -1):
    largest = 0
    for j in range(1,i+1):
        if(array[j]>array[largest]):
            largest = j
    swap(array,largest,i)
    print(array)
