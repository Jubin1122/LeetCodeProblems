'''
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal): 
            return False
        
        if s == goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            return False

        pairs = []
        for a, b in zip(s, goal):
            if a != b:
                pairs.append((a, b))
            if len(pairs) >= 3: 
                return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

obj = Solution()
s = "aaaab"
goal = "aaaab"
print(obj.buddyStrings(s, goal))