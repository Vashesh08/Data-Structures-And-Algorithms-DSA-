"""
Question:
        You are given the root of a binary search tree (BST) and an integer val.

        Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
        If such a node does not exist, return null.

        

        Example 1:


        Input: root = [4,2,7,1,3], val = 2
        Output: [2,1,3]
        Example 2:


        Input: root = [4,2,7,1,3], val = 5
        Output: []
        

        Constraints:

        The number of nodes in the tree is in the range [1, 5000].
        1 <= Node.val <= 107
        root is a binary search tree.
        1 <= val <= 107
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



"""
Method 1: Recursive Method
        It is a binary search tree, so values greater than in root are in the right subtree and values less than in the root are in the left subtree. 
        If root is None, return None
        If root.val is equal to val, then return the node(root)
        If root.val is greater than val to be searched, then search for the value in the left subtree.
        If root.val is less than val to be searched, then search for the value in the right subtree.
Time Complexity: O(log(n))
Space Complexity: O(log(n))
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        
        

"""
Method 2: Iterative Method
        It is a binary search tree, so values greater than in root are in the right subtree and values less than in the root are in the left subtree. 
        while root.val is not empty and root.val is not equal to val,
            If root.val is greater than val to be searched, then search for the value in the left subtree by putting root = root.left.
            If root.val is less than val to be searched, then search for the value in the right subtree by putting root = root.right.
        The while loop ends only when the values to be searched has been found or the value is not there(root becomes None).
        Either way the answer is stored in root, so return root.
Time Complexity: O(log(n))
Space Complexity: O(1)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            if root.val > val:
                root = root.left
            else:
                root = root.right
                
        return root
    
        
            
