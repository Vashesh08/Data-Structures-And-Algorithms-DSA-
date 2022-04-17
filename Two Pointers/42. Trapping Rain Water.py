"""
Question:
        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

        

        Example 1:


        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
        Example 2:

        Input: height = [4,2,0,3,2,5]
        Output: 9
        

        Constraints:

        n == height.length
        1 <= n <= 2 * 104
        0 <= height[i] <= 105

"""


"""
Method 1:
Time Complexity: O(n)
Space Complexity: O(1) 
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        res = 0
        length = len(height)
        left_prev = height[0]
        right_prev = height[length - 1]
        i = 1
        j = length - 2
        while i <= j:
            if left_prev < right_prev:
                if left_prev <= height[i]:
                    left_prev = height[i]
                else:
                    res += left_prev - height[i]
                i += 1
            else:
                if right_prev <= height[j]:
                    right_prev = height[j]
                else:
                    res += right_prev - height[j]
                j -= 1
            
        return res 
    