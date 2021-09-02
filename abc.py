'''
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

'''





def buddyStrings(s, goal):
        
    i = 0
    j = 0
    flag = True
    count = 0
        
    if len(set(s)) ==1 and len(set(goal)) ==1:
        return flag
    s = list(s)
    goal = list(goal)
        
    if len(s) ==2 and len(goal)==2:
        temp=s[i]
        s[i]= s[i+1]
        s[i+1] = temp
        sub_str = s[i:i+2]
        count += 1
        print(sub_str, goal[j:j+2])
                
        if sub_str == goal[j:j+2]:
            return flag
        else:
            return False
            
    while i < len(s) and j < len(goal):            
        if s[i] == goal[j]:
             
            i += 1
            j += 1
                
        else:
            
            temp=s[i]
            s[i] = s[i+1]
            s[i+1] = temp
            count +=1
            sub_str = s[i:i+2]
                
            if sub_str == goal[j:j+2] and count < 2:
                    
                i += 2
                j += 2
            elif count>=2:
                return False  
                    
            else:
                flag = False
                return flag
                
    return flag


print(buddyStrings("abcd", "abcd"))