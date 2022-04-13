"""
Question:
        Description
        Design an algorithm to encode a list of strings to a string. 
        The encoded string is then sent over the network and is decoded back to the original list of strings.

        Please implement encode and decode


        Example 1:

        Input: ["lint","code","love","you"]
        Output: ["lint","code","love","you"]
        Explanation:
        One possible encode method is: "lint:;code:;love:;you"


        Example 2:

        Input: ["we", "say", ":", "yes"]
        Output: ["we", "say", ":", "yes"]
        Explanation:
        One possible encode method is: "we:;say:
"""

# This question can be solved on lintcode question no 659


"""
Method 1: 
        Encoding is done by adding ":;" to the end.
        If a colon(":") is encountered during the encoding, then "::" is added to encode it.
        During decoding, the string is split wherever there is a ":;". 
        If "::" is encountered, just add ":" to the decoding list.  
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        y = ""
        for i in strs:
            if i == ":":
                y += ":"
            y += i +":;"
        
        return y.rstrip(":;")
        # return y

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        print(str)
        str = str.split(":;")
        decoded_list = []
        for i in str:
            if i == "::":
                decoded_list.append(":")
                continue
            decoded_list.append(i)

        return decoded_list



"""
Method 2: 
        Encoding is done by adding (length_of_digit+"#") to the start and then add the string.
        
        So start with the the first letter until you encounter a pound('#') sign. 
        This whole thing is the length(l) of the string that is actually to be decoded.
        Then the decoded string will be the next l(length) characters of the string.
        Repeat the whole procedure until you reach the end of the string.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        y = ""
        for i in strs:
            y += str(len(i)) + "#" + i
        
        return y
        # return y

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        i = 0
        decoded_list = []
        length = len(str)
        while i < length:
            n = ""
            while str[i] != "#":
                n += str[i]
                i += 1 
            n = int(n)
            i += 1
            decoded_list.append(str[i:i+n])
            i += n

        return decoded_list



