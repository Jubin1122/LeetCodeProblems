# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        
        translator = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                     4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

        out = ''
        for i in sorted(translator.keys(), reverse=True):
            if num - i >= 0:
                quotient, remainder = divmod(num, i)
                num = remainder
                out += translator[i] * quotient
                
        
        return out


