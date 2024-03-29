"""
Question:
        Given an integer array nums, 
        return true if any value appears at least twice in the array,
        and return false if every element is distinct. 

        Example 1:

        Input: nums = [1,2,3,1]
        Output: true
        Example 2:

        Input: nums = [1,2,3,4]
        Output: false
        Example 3:

        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
        

        Constraints:
            1 <= nums.length <= 105
            -109 <= nums[i] <= 109
"""


"""
Method 1: Using Dictionary 
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                return True
            dictionary[i] = 1
            
        return False


"""
Method 2: Using Sets 
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        sets = set()
        for i in nums:
            if i in sets:
                return True
            sets.update([i])
            
        return False

