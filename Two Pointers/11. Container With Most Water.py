"""
Question:
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.

        

        Example 1:


        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
        Example 2:

        Input: height = [1,1]
        Output: 1
        

        Constraints:

        n == height.length
        2 <= n <= 105
        0 <= height[i] <= 104
"""


"""
Method 1: Naive/Brute Force Approach
        Loop through each element of the height.
            For each element loop from the next element in the array to the last element of the array and 
            check each combination and how much water does each portion holds. 
            If that capacity exceeds the maximum_capacity found yet, then replace the maximum_capacity with the current capacity.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0 
        length = len(height)
        for x1 in range(length):
            for x2 in range(x1, length):
                value = (x2-x1) * min(height[x1], height[x2])
                if value > maximum:
                    maximum = value
        return maximum



"""
Method 2: Two Pointer Approach
        Keep two pointers 'i'=0 and 'j'=(length_of_array - 1).
        while i < j:
            Since index position also decides the area of a rectangle, 
            Therefore , the more farther the pointer are there, the more the area of the rectangle would be.
            We first calculate the area for the farthest, positions of both the pointer are at start and end.
            Remember that if we move any pointer then the width of the rectangle decreases. Hence, we move the pointer whose
            height is lesser (lower_height) and we move this pointer until we find a height which is greater than this 
            this lower_height because heights lower than the lower_height will have less area than the before one because 
            width also decreases(due to the moving of the pointers) and height is also less than the previous. 
            Once, we find a height greater than the lower_height, we recalculate the area and check if it is greater than the maximum_area
            calculated until now.
            If it is, then replace the maximum_height.
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        maximum_water = 0
        while i <= j:
            water_area = min(height[i], height[j]) * (j-i) 
            if water_area > maximum_water:
                maximum_water = water_area
            if height[j] > height[i]:
                min_height = height[i]
                while height[i] <= min_height and i <=j:
                    i += 1
            else:
                min_height = height[j]
                while height[j] <= min_height and i <=j:            
                    j -= 1
            
        return maximum_water
