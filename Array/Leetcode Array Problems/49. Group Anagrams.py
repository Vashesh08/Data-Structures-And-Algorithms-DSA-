"""
Question:
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

        

        Example 1:

        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        Example 2:

        Input: strs = [""]
        Output: [[""]]
        Example 3:

        Input: strs = ["a"]
        Output: [["a"]]
        

        Constraints:

        1 <= strs.length <= 104
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.
"""


"""
Method 1: Using Arrays/Lists
          For every word, sort the word and
          it will check if a the sorted word already exists in a list(empty_list2).
          If it doesn't exist, the sorted word will append as a list to the list(empty_list2) and the word
              will append as a list of word to another list(empty_list).
          If it exists, the sorted word will append to the list(empty_list2) at that particular positon and the word will 
              append to another list(empty_list).
Time Complexity: O(n*m)
Space Complexity: O(n)
      n = length of array strs
      m = length of every word in strs
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        empty_list2 = []
        empty_list3 = []
                
        for j in range(len(strs)):
            words = sorted(strs[j])
            for k in range(len(empty_list3)):
                if empty_list3[k][0] == words:
                    empty_list2[k].append(strs[j])
                    empty_list3[k].append(words)
                    break
            else:
                empty_list2.append([strs[j]])
                empty_list3.append([words])
        
        return empty_list2

    
"""
Method 2: Using Hashmaps/Dictionary
          Create a dictionary of each word with alphabets as keys and 
          incrementing the values(starting from zero) for each occurrence of the alphabet
          For every word, it will check if a similar dictionary already exists in a list of dictionaries(empty_list2).
          If it doesn't exist, the dictionary will append as a list of dictionaries to the list(empty_list2) and the word
              will append as a list of word to another list(empty_list).
          If it exists, the dictionary will append to the list(empty_list2) at that particular positon and the word will 
              append to another list(empty_list). 
Time Complexity: O(n*m)
Space Complexity: O(n)
      n = length of array strs
      m = length of every word in strs
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        empty_list = []
        empty_list2 = []
        
        for i, word in enumerate(strs):
            empty_dict = {}
            for k in word:
                empty_dict[k] = empty_dict.get(k,0) + 1
            for j in range(len(empty_list2)):
                if empty_dict == empty_list2[j][0]:
                    empty_list[j].append(strs[i])
                    empty_list2[j].append(empty_dict)
                    break
            else:        
                empty_list.append([strs[i]])
                empty_list2.append([empty_dict])
            
        return empty_list


"""    
Method 3: Using Strings
          Create an empty dictionary  
          Loop through each word in the string 
          Create a string of the sorted(word)
          Check if the sting exists in the dictionary as a key 
          If it doesn't exist, put the sorted word as the key and the value as the word(in the form of a list) itself 
          If it exists, then append the word to the value of the dictionary[sorted(key)] 
          Return the values of the dictionary as the answer
Time Complexity: O(n*m*log(m))
Space Complexity: O(n)
      n = length of array strs
      m = length of every word in strs
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        anagrams = {}
        
        for word in strs:
            key = "".join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
                
        return anagrams.values()        
        