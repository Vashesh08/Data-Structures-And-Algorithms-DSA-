"""
Question:
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.

        

        Example 1:

        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.
        Example 2:

        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.
        Example 3:

        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.
        

        Constraints:

        1 <= s.length <= 2 * 105
        s consists only of printable ASCII characters.
"""


"""
Method 1: Using String
        Loop through each character in the string s and check if each character is alphanum or not.
        If it is alphanum, check if it is uppercase or lowercase.
            If it is uppercase, convert it into lowercase. Else, pass.
            Append this character to an empty string.
        Else, Move to the next character.

        At the end, check if it is a palindrome or not.
Time Complexity: O(n) # To loop through the array once
Space Complexity: O(n) # To store the character in another string 'y'
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        length = len(s)
        y = ""
        while i < length:
            if s[i].isalnum():
                if s[i].isupper():
                    y+=s[i].lower()
                else:
                    y += s[i]
            i += 1
        
        return y[::1] == y[::-1]


"""
Method 2: Two Pointer Approach
        Take two pointers one at the start('i') and one at the end('j)
        Loop until i < j:
            Move the i pointer to the right until you encounter a character which is alphanumeric
            Move the j pointer to the left until you encounter a character which is alphanumeric
            Now check if character at 'i'th position is equal to the character at 'j'th position
            If it is not equal, it is not palindrome, return 'False'
        If it comes out of the loop, all characters have been checked and it is a palindrome.
        Therefore, return True.
Time Complexity: O(n) # To loop through the array once
Space Complexity: O(1) 
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():                    
                    i += 1
                    j -= 1
                else:
                    return False
            elif s[j].isalnum():
                i += 1
            elif s[i].isalnum():
                j -= 1
            else:
                i += 1
                j -= 1
        
        return True
    
# A more readable version of the above code would be
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():                    
                    i += 1
                    j -= 1
                else:
                    return False
                continue
            elif s[j].isalnum():
                i += 1
                continue
            j -= 1
            
        
        return True
        


### NOTE: You can implement the alnum function as follows (if using built-in string functions is not allowed to use in interviews)
def isalnum(c:str):
    return (ord('A') <= ord(c) <= ord('Z')) or \
            (ord('a') <= ord(c) <= ord('z')) or \
            (ord('0') <= ord('c') <= ord('9'))
 