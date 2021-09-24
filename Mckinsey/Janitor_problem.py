'''
1.	Efficient Janitor
Find the minimum number of groups who's sum of each group is at max 3, and every element must be in a group.
Given an Array like: [1.01, 1.01, 3.0, 2.7, 1.99, 2.3, 1.7]
return the minimum number of groups, in this case it would be 5 groups: (1.01 , 1.99), (1.01, 1.7), (3.0), (2.7), (2.3)
Constraint: all elements are between 1.01-3 inclucsive, and each groups sum is at max 3

'''

def efficientJanitor(weight):

    weight.sort()
    left =0
    right = len(weight) -1
    count = 0 

    while left <= right:
        if left == right:
            count += 1
            break

        if weight[left] + weight[right] <= 3.0:
            left += 1
            right -= 1
            count += 1

        else:
            right -= 1
            count += 1



    return count
    


out = efficientJanitor([1.01, 1.01, 3.0, 2.7, 1.99, 2.3, 1.7])
print(out)