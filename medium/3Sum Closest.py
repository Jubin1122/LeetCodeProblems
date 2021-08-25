
'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
'''

def threeSumClosest(nums, target):
    nums = sorted(nums)
        
    n = len(nums)
    close = None
    for i in range(n):
           
        left = i+1
        right = n-1
                
        while left < right:
                    
            tot = nums[i] + nums[left] + nums[right]
                    
            if close is None:
                    close = tot
            else:
                if abs(tot-target) < abs(close -target):
                    close = tot
                    
                if abs(tot-target) == 0 or abs(close-target) == 0:
                    return target                           
                    
            if tot < target:
                left +=1
                        
            elif tot >target:
                right -= 1
                        
            else:
                left += 1
                right -= 1
                        
    return close

nums = [1,2,4,8,16,32,64,128]
target = 82
out = threeSumClosest(nums, target)
print(out)



    