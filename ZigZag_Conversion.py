"""
-- ZigZag Conversion---

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2: return s
        pos = 1
        step = 1
        lines = {}
        for char in s:     
            if pos not in lines:
                lines[pos] = char
            else:
                lines[pos] += char
            pos += step
            if pos == 1 or pos == numRows:
                step *= -1
                
        sol = ''.join(lines.values())
        return sol


out = Solution()
print(out.convert('PAYPALISHIRING', 3))