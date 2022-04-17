"""
Question:
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.

        Your solution must use only constant extra space.

        

        Example 1:

        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
        Example 2:

        Input: numbers = [2,3,4], target = 6
        Output: [1,3]
        Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
        Example 3:

        Input: numbers = [-1,0], target = -1
        Output: [1,2]
        Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
        

        Constraints:

        2 <= numbers.length <= 3 * 104
        -1000 <= numbers[i] <= 1000
        numbers is sorted in non-decreasing order.
        -1000 <= target <= 1000
        The tests are generated such that there is exactly one solution.
"""



"""
Method 1: Naive Method
        Loop through the array 'numbers'. For every element, loop through the array once more from that particular
          index position to find out if another element exists such that the sum of both the elements 
          equal to the target.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        length = len(numbers)
        for i in range(length):
            for j in range(i+1, length):
                if numbers[i] + numbers[j] == target:
                    return i+1,j+1
# The above method will give a Time Limit Exceeded Error on LeeetCode             


"""
Method 2: Using Dictionaries 
        Loop Through The array. For every element, find out its complement(target - element) which needs to be in the array.
          Check if the complement is in the keys of the dictionary. If it does not exist, stre the element in the dictionary
          with element as the key and its index position as value. If the complement exists, return the index position of the
          element and the value of the complement in the dictionary
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        empty_dict = {}
        for i in range(len(numbers)):
            complementary = target - numbers[i]
            if complementary in empty_dict:
                return [empty_dict[complementary] + 1, i + 1]
            empty_dict[numbers[i]] = i
        
            
"""
Method 3: Optimal Method - Two Pointer Approach
        The array is sorted. Using this to our advantage we devise a solution.
        Take two pointers one at the start('i') of the 'numbers' array and one at the end('j) of the 'numbers' array.
        Loop Until 'i' < 'j':
            Now, sum the numbers at the 'i'th location and the 'j'th location of the array. 
            If the sum is greater than the target, then decrement the 'j'th pointer (move the 'j'th pointer to the left).
            Else if the sum is less than the target, then increment the 'i'th pointer (move the 'i'th pointer to the right).
            Else if the sum is equal to the target, then return the 'i+1' and 'j+1' index position because 1-index based question.
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            search = numbers[i] + numbers[j]
            if search == target:
                return [i+1,j+1]
            elif search < target:
                i += 1
            else:
                j -= 1
            
        