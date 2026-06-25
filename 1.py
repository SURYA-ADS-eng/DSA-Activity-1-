""""
1)TWO SUMS (1)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


#simple level begginer method
list_1 = [2,3,4]
target_1 = 6

for i in range(len(list_1)):
    for j in range(i+1, len(list_1)):
        if((list_1[i] + list_1[j]) == target_1):
            print([i,j])

#interview level or coding level method
list_2 = [4,5,7,8,2]
target_2 = 12

d = {}
for i in range(len(list_2)):
    diff = target_2 - list_2[i]

    if diff in d:
        print([d[diff],i])
        break

    d[list_2[i]] = i


