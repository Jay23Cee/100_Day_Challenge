def binarysearch(alist, item):
    
    if len(alist) ==0:
       return False
    else:
        mid = len(alist)//2
        if alist[mid]==item:
            return True
        else:
            if item < alist[mid]:
              return binarysearch(alist[:mid], item)
            else:
               return binarysearch(alist[mid+1:], item)
 



print("hello")

testlist = [0,1,2,8,13,17,19,32,42]
print(binarysearch(testlist,32))