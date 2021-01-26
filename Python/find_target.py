class Solution(object):
    def __init__(self):
            print()
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        send_back = []
        
        for x in range(size):  
            
            if not x == size-1:
                for i in range(size):
                    i=i+x+1
                    if  i > size-1:
                        break
                    else:
                        total = nums[x]+nums[i]
                        print(total,i,x)
                        if total == target:
                            print(x,i, total)
                            send_back.append(x)
                            send_back.append(i)
                            return send_back
                         
                        else: 
                            continue


print( Solution().twoSum([2,5,7,3,6], 9))