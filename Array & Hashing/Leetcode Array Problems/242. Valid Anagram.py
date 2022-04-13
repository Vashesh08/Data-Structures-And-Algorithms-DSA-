"""
Question:
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.

        

        Example 1:

        Input: s = "anagram", t = "nagaram"
        Output: true
        Example 2:

        Input: s = "rat", t = "car"
        Output: false
        

        Constraints:

        1 <= s.length, t.length <= 5 * 104
        s and t consist of lowercase English letters.
        

        Follow up: What if the inputs contain Unicode characters? 
        How would you adapt your solution to such a case?
"""


"""
Method 1: Sorting the strings and then comparing if each element of string 's' is same as string 't'
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return t == s


"""
Method 2: Using A Dictionary to keep a count of the occurence of each alphabet in string 's'
          and then reducing the count of each alphabet in the string 't'. If the alphabet from string 't'
          doesn't exist in dictionary or the count goes below zero, return False. If count equals zero,
          remove that key from the dictionary. 
          If the dictionary is empty at the end, it is an anagram. Therfore, return True. Else, 
          it is not an anagram. Therefore, return False
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        empty_list = {}
        for i in s:
            empty_list[i] = empty_list.setdefault(i,0) + 1
        
        for i in t:
            empty_list[i] = empty_list.get(i, -1) - 1
            if empty_list[i] < 0:
                return False
            if empty_list[i] == 0:
                del empty_list[i]
            
        if len(empty_list) == 0:
            return True
        return False
