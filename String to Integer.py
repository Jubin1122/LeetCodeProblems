import re
"""
def myAtoi(s): 
    pat1 = r'[\s+]?[-]?[0-9]+'
    m = None
    num = None


    if re.search(r'^\.',s) or '-+' in s or '+-' in s or re.search('\s\-\s', s) or re.search('\s\+\s', s) or re.search(r'^[a-zA-Z]',s) or not(re.search(r'[\s+]?[0-9]*[\+]{2}', s)) or re.search(r'[\-]{2}', s):
        return 0

    
    if re.search(pat1,s):
        m =re.search(r'[-]?[0-9]+',s).group(0)
        
    print(m)
    if m != None and not(m.startswith('.')): 
        if m.startswith('+') or m.startswith('-') or m[0].isdigit():
            num = int(m)
            if num < -2 ** 31:
                num = -2 ** 31
            elif num > (2**31) - 1:
                num = (2**31) - 1
    if m is None or m.startswith('.'):
        return 0
    
    return num
"""
def myAtoi(s):
    try:
        match = re.search('^[ \+\-]*\d+', s)
            # restrict the value to be between -2147483648 and 2147483647
        return min(max(-2147483648, int(match.group())), 2147483647)
    except:
        return 0

s = " 1"
print(myAtoi(s))