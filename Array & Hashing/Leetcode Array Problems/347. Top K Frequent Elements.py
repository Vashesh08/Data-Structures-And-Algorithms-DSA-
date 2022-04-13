"""
Question:
        Given an integer array nums and an integer k, return the k most frequent elements. 
        You may return the answer in any order.

        

        Example 1:

        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        Example 2:

        Input: nums = [1], k = 1
        Output: [1]
        

        Constraints:

        1 <= nums.length <= 105
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.
        

        Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


"""
Method 1: Loop through the array 'nums' and store the number of occurences of each number in a list('list_of_occurences')
            of tuples of (occurence of the number, number)
          Sort the list('list_of_occurences'). Then append the result of occurences of the first k elements to a list('result')
          and return this list.
Time Complexity: O(nlogn) 
Space Complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        list_of_occurences = []
        dictionary = {}
        for i in nums:
            if i in dictionary:
                list_of_occurences[dictionary[i]][0] += 1
            else:
                dictionary[i] = len(list_of_occurences)
                list_of_occurences.append([0,i])
    
        result = []
        list_of_occurences = sorted(list_of_occurences, reverse=True) # O(nlogn) for sorting the list
        i = 0

        while k > 0:
            result.append(list_of_occurences[i][1])
            i += 1
            k -= 1
            
        return result


"""
Method 2: Using Heap 
            Loop through the array 'nums' and store the occurence of each number in a dictionary('result')
            with number as key and occurence of the number as its value
            Take another array 'heap' where you store only 'k' number of elements. Loop through the array 'nums'
            and store the first 'k' distinct elements in this array('heap'). 
            Store the elements in such a way that the first element has the highest occurence and the second element te second highest
            and so on. 
            After storing the distinct elements in 'heap', check if the next element has an occurence greater than the last element
             of the heap using the dictionary.
            If yes, then loop through the heap and store it in correct position.
            Else, move to next element.
            Return the array 'heap'
Time Complexity: O(n*k)
Space Complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = {}
        heap = [] 
        i = 0
        for num in nums:
            result[num] = result.get(num,0) + 1
            if i < k and result[num] == 1:
                i += 1
                heap.append(num)
            else:
                if num in heap:
                    heap.remove(num)
                    heap.append(num)
                for t, value in enumerate(heap):
                    if result[num] > result[value]:
                        heap.insert(t,num)
                        heap.pop()
                        break
        return heap
    

"""
Method 3: Using Bucket Sort
            Create an empty 2D-Array with order 1 x k ('result').
            Loop through the array 'nums' and store the occurence of each number in a dictionary('dictionary')
            with number as key and occurence of the number as its value
            Now, Loop through the dictionary and store the number(dictionary.key) at the index of 
            dictionary.value(count of the occurence of that number) in te 2D-Array.
            Now Loop through the 2-D array in the reverse order and put the number in the array 'answer' and
            as soon as 'k' numbers are there, return the answer.
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        dictionary = {}
        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
            result.append([])  

        for key, value in dictionary.items():
            result[value-1].append(key)
            
        i = 0
        j = 1
        answer = []
        
        while i < k:
            if len(result[-j]) > 0:
                for element in result[-j]:
                    answer.append(element)
                    i += 1
                    if i == k:
                        return answer
            j += 1
            
        return answer    