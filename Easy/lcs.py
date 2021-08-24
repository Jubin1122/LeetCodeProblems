'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

'''

def threeSum(nums):
        
    ar = []
    nums = sorted(nums)

    n = len(nums)
    if n == 0 or n == 1:
        return []
    #print(n)
        
    for i in range(n):
        left = i+1
        right = n-1
            
        while left < right:
                
            total = nums[i] +nums[left] +nums[right]
            if total == 0:
                x = [nums[i], nums[left], nums[right]]
                if x not in ar:
                    ar.append(x)
                #print(ar)
                left += 1
                right -=1
                    
            if total < 0:
                left += 1
                    
            if total > 0:
                right -= 1
                    
    return ar

out  = threeSum([-1,0,1,2,-1,-4])
print(out)