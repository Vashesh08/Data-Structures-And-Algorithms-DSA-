"""
Question:
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        

        Example 1:

        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Example 2:

        Input: nums = []
        Output: []
        Example 3:

        Input: nums = [0]
        Output: []
        

        Constraints:

        0 <= nums.length <= 3000
        -105 <= nums[i] <= 105
"""


"""
Method 1: Naive Method
        First, sort the array 'nums'.
        Loop through each number in the sorted array 'nums'.
        For each number, we must find two other numbers in the array 'nums' such that
            the sum of those two other numbers is negative of every number in the array 'nums'.
        Therefore, we must loop through the array again from the next position.
        While doing so, we have to make sure we don't encounter the same element twice.('left' and 'right')  
        We use the two sum approach in the this loop.
            TWO SUM APPROACH:
                Take two pointers one at the start('i') of the 'numbers' array and one at the end('j) of the 'numbers' array.
                Loop Until 'i' < 'j':
                    Now, sum the numbers at the 'i'th location and the 'j'th location of the array. 
                    If the sum is greater than the target, then decrement the 'j'th pointer (move the 'j'th pointer to the left).
                    Else if the sum is less than the target, then increment the 'i'th pointer (move the 'i'th pointer to the right).
                    Else if the sum is equal to the target, then return the 'i+1' and 'j+1' index position because 1-index based question.
 
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        result = []
        nums = sorted(nums)
        k = 0
        while k < length-1:
            target = - nums[k]
            i = k + 1
            j = length - 1
            center = nums[k]
            while i < j:
                left = nums[i]
                right = nums[j]   
                if nums[i] + nums[j] == target:
                    result.append([nums[k],nums[i],nums[j]])
                    while left == nums[i] and i < j:
                        i += 1
                    while right == nums[j] and i<j:
                        j -= 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    i += 1
            while center == nums[k] and k < length -1:
                k += 1
            
        
        return result
                


# Another way for same approach
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums = sorted(nums)
        length = len(nums)
        prev = None
        for i in range(length):
            if prev == nums[i]:
                continue
            target = - nums[i]    
            prev = nums[i]
            j = i + 1
            k = length - 1
            while j < k:
                sum_two = nums[j] + nums[k] 
                if sum_two < target:
                    j += 1
                elif sum_two > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return result