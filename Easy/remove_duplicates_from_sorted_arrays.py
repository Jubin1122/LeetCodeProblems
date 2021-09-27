
class Solutions:
     def removeDuplicates(self, nums):
        """
        # with an extra space, Space Complexity O(n)

        n = len(nums)
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1

            else:
                dic[i] += 1

        arr = [k for k in dic.keys()]
        m = len(dic)

        if n-m > 0:
            return len(dic), arr + list('_'*(n-m))

        else:
            return len(dic), arr
        """
        """

        # 2. Space complexity, O(1) 
        s = 0

        while s < len(nums) - 1:
            print(s)
            if nums[s+1] != None:
                if nums[s] == nums[s+1]:
                    nums.pop(s)
                    s += 1
                    #print(nums)

                elif nums[s] == nums[s-1]:
                    nums.pop(s-1)

                else:
                    s += 1
            else:
                break
        return nums
        """

        # Only count the unique values
        numsIndex = 1
        for index in range(len(nums)):
            if index == 0:
                continue
            elif nums[index] != nums[index-1]:
                
                nums[numsIndex]=nums[index]
                numsIndex+=1
        

        return numsIndex

out = Solutions()
arr = out.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(arr)

        