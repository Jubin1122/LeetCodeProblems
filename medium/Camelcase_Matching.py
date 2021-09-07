'''
Camelcase Matching

Given an array of strings queries and a string pattern, 
return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

A query word queries[i] matches pattern if you can insert lowercase English letters 
pattern so that it equals the query. Y
ou may insert each character at any position and you may not insert any characters.

Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll"

'''


class Solution:
    def camelMatch(self, queries, pattern):
        
        ch = ''
        ar = []
        for i in pattern:
            if i.isupper():
                ch += i
        
        
        for q in queries:
            flag = True
            temp= ''
            for i in q:    
                if i.isupper():
                    temp += i
                
            if temp != ch:
                ar.append(False)
                continue
            
            ts = []
            ts[:0] = pattern

            while ts:

                ele  = ts[0]
                if ele in q:
                    ind  = q.index(ele)
                    q = q[ind+1:]
                    ts.pop(0)
                else:
                    flag = False
                    ar.append(flag)
                    break

            if flag == True:
                ar.append(flag)

        return ar

obj  = Solution()
out  =obj.camelMatch(["ForceFeedBack","FrameBuffer","FooBar","FooBarTest","FootBall"] , "FoBa")

print(out)