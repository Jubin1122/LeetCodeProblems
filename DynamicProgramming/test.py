def sol(height):
    i = 1
    j = len(height)
    max = 0
    area = 0
    while i < j and i !=j:
        
        #cor_set1 = (i,height[i-1])
        #cor_set2 = (j, height[j-1])

        #length = cor_set2[0]- cor_set1[0]
        #width = min(cor_set2[1],cor_set1[1])
        area = (j-i) * min(height[i-1], height[j-1])
        #print(area)
        if max < area:
            max = area
        
        if height[i-1] < height[j-1]:
            i +=1 
        
        elif height[i-1] > height[j-1]:
            j -=1
        
        #elif height[i-1] == height[j-1]:
        else:
            i +=1
        
        #print(f'{cor_set1}\n{cor_set2}')
    return max

height = [1,8,6,2,5,4,8,3,7]
obj = sol(height)
print(obj)