'''
Iterative Letter Combinations of a Phone Number

Approach: Depth first Search(Map datastructure)
Python: Deque

Time Complexity: O(N)
Auxiliary Space: O(N)
'''
from collections import deque
class Solution:
    def letterCombinations(self, digits):

        number = list(digits)
        table= ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        final_out = self.possbile_combn(number,table)

        return final_out

    def possbile_combn(self, number,table):

        q = deque()
        ls = list()
        q.append('')
        n = len(number)
        while len(q) !=0:
            s = q.pop()

            if len(s) == n:
                ls.append(s)

            else:
                for letter in table[int(number[len(s)])]:
                    q.append(s + letter)
                
            
        return ls
        



obj = Solution()
digits = '23'
print(obj.letterCombinations(digits))


