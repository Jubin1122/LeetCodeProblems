class Solution:
    def strStr(self, haystack, needle):
        
        ind = 0
        cnt = 0 
        start_ind = 0
        
        if len(needle) == 0 and len(haystack)==0:
            return 0
        
        for i in needle:
            
            for j in range(cnt, len(haystack)):
                
                if i == haystack[j]:
                    
                    cnt = j +1

                    ind += 1
                    if start_ind == 0:
                        start_ind = j
                    break
                    
            if ind ==0:
                return -1
            
        
        if ind == len(needle):
            return start_ind

haystack, needle = "abc", "c"
out = Solution()
print(out.strStr(haystack, needle))