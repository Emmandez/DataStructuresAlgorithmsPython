array = [20, 35, -15, 7, 55, 55, -22]

def swap(array, i, j):
    if(i == j):
        return

    temp = array[i]
    array[i] = array[j]
    array[j] = temp  

lastUnsortedIndex = len(array)-1


for i in range(lastUnsortedIndex,0,-1):
    for j in range(i):
        if(array[j]>array[j+1]):
            swap(array,j,j+1)
            print(array)
    




      