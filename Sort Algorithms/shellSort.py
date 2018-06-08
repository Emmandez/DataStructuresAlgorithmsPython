array = [20, 35, -15, 7, 55, 1, -22]

print(array)

gap = len(array)//2
while gap > 0:
    
    for i in range(gap,len(array)):
        newElement = array[i]
        j = i
        while(j>=gap and array[j-gap]>newElement):
            array[j] = array[j-gap]
            j-=gap
        array[j] = newElement


    gap = gap//2

print(array)    
 