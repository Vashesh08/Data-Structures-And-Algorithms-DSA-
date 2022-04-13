"""
Question:
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.

        

        Example 1:

        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
        Example 2:

        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9
        

        Constraints:

        0 <= nums.length <= 105
        -109 <= nums[i] <= 109
"""


"""
Method 1: Sort the array and check previous number in the array with the current array.
        If the current number is one greater than the previous number, increment the count of the current_maximum('maximum')
        Else if the current number is same as the previous number, do nothing.
        Else check if the count of the current_maximum is greater than the maximum_value. 
            If it is, then put the maximum_value in the current_maximum variable.
            If not, then do nothing(pass)
            Reset the value of the current_maximum('maximum' variable) to 1 and loop until you have checked all the elements once.
Time Complexity: O(nlogn) # For Sorting
Space Complexity: O(1)
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0: # if the array is empty return 0
            return 0
        nums = sorted(nums)
        i = 0
        maximum_value = maximum = 1
        length = len(nums)
        while i < length - 1:
            if nums[i] == nums[i+1] - 1:
                maximum += 1  
            elif nums[i] == nums[i+1]:
                pass
            else:        
                if maximum > maximum_value:
                    maximum_value = maximum
                maximum = 1
            i += 1
        if maximum > maximum_value:
            maximum_value = maximum
                
        return maximum_value


"""
Method 2: First, store each number of the array as key and value=1 in the dictionary. 
        
        Again loop over the array. Now check if the value of each number in the array is 1 in the dictionary.
        Value of a number in dictionary = 1 indicates number exists in a dictionary but is not visited
        If the value is not 1, move to the next element.
        If the value is 1, then put the maximum of current range(current_maximum) as 1 and change the value of the dictionary as 2
            Value of a number in dictionary = 2 indicates number exists in a dictionary and has been visited
            Now check the same for adjacent elements. Say the number that was visited was 100. 
            Then now check the same for 101, 102... and so on 
                and mark the node as visited by making the value of that key in dictionary as 2.
                Keep on incrementing current_maximum by 1 for each node vsited
            
            At the same time check the same for 99, 98... and so
                on and mark the node as visited by making the value of that key in dictionary as 2.
                Keep on incrementing current_maximum by 1 for each node vsited
            
            Now check if the current_maximum exceeds the overall maximum value('maximum_value'). 
                If it does, then store the value of the current_maximum in the overall maximum value('maximum_value').Else, pass.

        Alternatively you can use sets as well. The implementation may change a bit though.
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        dictionary = {}
        for i in nums:
            dictionary[i] = 1
            
        maximum_value = 0
        for i in nums:
            if dictionary.get(i, 0) == 1: # check for i = 100
                maximum = 1
                dictionary[i] = 2
                j = i + 1
                k = i - 1
                while dictionary.get(j, 0) == 1: # check for i = 101, 102...
                    dictionary[j] = 2
                    maximum += 1
                    j += 1

                while dictionary.get(k, 0) == 1: # check for i = 99, 98...
                    dictionary[k] = 2
                    maximum += 1
                    k -= 1

                if maximum_value < maximum:
                    maximum_value = maximum
                
        return maximum_value
