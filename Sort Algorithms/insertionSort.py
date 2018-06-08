array = [20, 35, -15, 7, 55, 1, -22]
print(array)

for i in range(1,len(array)):
    newElement = array[i]
    j = i
    # swap the items if the new element is lesser than
    # one of the item we already have
    while j>0 and array[j-1]>newElement:
        array[j] = array[j-1]
        j = j-1
    array[j] = newElement

print(array)
    
