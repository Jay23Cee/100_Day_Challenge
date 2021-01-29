
def sort(arr):
    arr_size = len(arr)
    beg =0
    end= arr_size-1 
    new_list = [None]*arr_size

    for x in range(arr_size):
        if arr[x] %2 ==0:
            new_list[beg]= arr[x]
            beg = beg+1
        else:
            new_list[end]= arr[x]
            end = end-1
    
    return new_list


arr1 = [5,2,4,6,7,9]

print(sort(arr1))
