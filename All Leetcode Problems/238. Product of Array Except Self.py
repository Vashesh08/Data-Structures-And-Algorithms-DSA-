"""
Question:
        Given an integer array nums, return an array answer such that answer[i] is equal to the product 
        of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.

        

        Example 1:

        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        Example 2:

        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]
        

        Constraints:

        2 <= nums.length <= 105
        -30 <= nums[i] <= 30
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        

        Follow up: Can you solve the problem in O(1) extra space complexity?
         (The output array does not count as extra space for space complexity analysis.)
"""


"""
Method 1: Naive Method
        Loop through the array 'nums'. For each number in nums, loop through the array again
         and multiply all the numbers except number(the one at that particular index position)
        Append the result in the result array  
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = []
        for i in range(length):
            product = 1
            for j in range(length):
                if j != i:
                    product *= nums[j]
            result.append(product)
        return result
# This Solution gives Time Exceeded Error in Leetcode


"""
Method 2: Division Method
          Multiply all the elements of the array and store it in 'product'
          Loop Through the array and divide the number at the index position.
          Be carful with the occurences of zero in the array.
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = []
        boolean = 0
        product = 1
        for i in range(length):
            if nums[i] != 0:
                product *= nums[i]
            else:
                boolean += 1
                
        for j in range(length):
            if nums[j] != 0:
                if boolean > 0:
                    result.append(0)
                else:
                    result.append(product//nums[j])
            else:
                if boolean > 1:
                    result.append(0)
                else:
                    result.append(product)
        return result
# This method passes Leetcode but violates the condition that division operator must not be used.



"""
Method 3: Optimal Method with extra space Complexity
            Create a prefix array('prefix_product') and a postfix array('suffix_product')
            
            The prefix array multiplies all the elements of the array before the given index and stores it. 
            This is done in the first pass(for loop).
            
            The postfix array multiplies all the elements of te array after the given index and stores it.
            This can be done in one pass(second for loop) when done in reverse order.
             
            In the last for loop, the elements of the prefix array are multiplied with the elements of the postfix 
            array and the result is stored in the 'result' array.
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_product = [1,]
        suffix_product = [1,]
        length = len(nums)
        product = 1
        for i in range(length-1):
            product *= nums[i]
            prefix_product.append(product)
        product = 1
        for i in range(1,length):
            product *= nums[-i]
            suffix_product.insert(0, product)
        result = []
        for i in range(length):
            result.append(prefix_product[i]*suffix_product[i])
        
        return result



"""
Method 4: Optimal Method
            This is an optimisation over the method 3 approach in terms of space complexity.
            The idea is similar to the method 3.

            However, instead of creating the prefix and postfix array, only create the 'result' array, 
            store the prefix values in the result 'array', multiply it with the postfix value and return the 'result' array
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1,]
        length = len(nums)
        product = 1
        for i in range(length-1):
            product *= nums[i]
            result.append(product)
        product = 1
        for i in range(1,length+1):
            result[-i] *= product
            product *= nums[-i]
                    
        return result