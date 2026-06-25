#easy begginer level program

""""
3)CONTAINS DUPLICATE (217)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
"""

nums = [1,2,3]

found = False

for i in range(len(nums)):
    for j in range(i+1, len(nums)):

        if(nums[i] == nums[j]):
            found = True
            break

    if found:
        break

print(found)



#interview level or coding level program

nums_1 = [1,2,3,4,5,2,3]

seen = set()

for num in nums_1:

    if num in seen:
        print(True)
        break

    seen.add(num)

else:
    print(False)

