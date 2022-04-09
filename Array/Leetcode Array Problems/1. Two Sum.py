"""
Question:
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.

        

        Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]
        

        Constraints:

        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.
        

        Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


# Method 1: Loop through the array. For every element, loop through the array once more from that particular
#           index position to find out if another element exists such that the sum of both the elements 
#           equal to the target.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i] + nums[j] == target:
                    return i, j
                



# Method 2: Loop Through The array. For every element, find out its complement(target - element) which needs to be in the array.
#           Check if the complement is in the keys of the dictionary. If it does not exist, stre the element in the dictionary
#           with element as the key and its index position as value. If the complement exists, return the index position of the
#           element and the value of the complement in the dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        empty_dict = {}
        for i, num in enumerate(nums):
            find_target = target - num
            if empty_dict.get(find_target, -1) >= 0:
                return empty_dict[find_target], i
            empty_dict[num] = i
        

