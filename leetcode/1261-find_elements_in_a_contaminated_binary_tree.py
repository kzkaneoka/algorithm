# QUESTION: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    # We need to iterate through the nodes in the tree, and fix the node's values.
    # The node's value determines by its parent.
    # Therefore, when we iterate through each node, we fix the value of node's children, not the value of node itself.
    # There are many ways of iterating tree. I used stack for iteration.
    # In python, list can be used as stack. https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
    def __init__(self, root: TreeNode):
        self.root = root
        # self.values = set()
        
        root.val = 0
        nodes = [root]
        while nodes:
            node = nodes.pop()
            # self.values.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                nodes.append(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                nodes.append(node.right)
        

    # Because we iterate through every node in the __init__function, we can create a set and store each node's value.
    # Then, in the find function, we can check if the target is in the set or not easily.
    # However, what if we cannot use the set?
    # What if the size of each node's value is, let's say, 100 gigabytes?
    # What if the number of nodes is huge?
    # Maybe, we cannot store all values in the set, and need to think about a different way to check if the target is in the tree or not.

    #                 0
    #             /       \
    #         1               2
    #     /       \       /       \
    #    3         4     5         6

    # In this tree, there are some interesting properties.
    #     Each value is always at the specific location, e.g., value 1 is always at the left child of 0.
    #     We can calculate the parent's value of the node -> (node.val - 1) divide by 2.
    #     If the node is odd number -> the node is always left child of the parent.
    #     If the node is even number -> the node is always right child of the parent.

    # Let's say 4 is our target value.
    #     We know 4 is always at the right child of 1.
    #     We know 1 is always at the left child of 0.
    #     It means we know the target 4 is in the tree if we can walk through this path, 1 -> 4, from the root.
    #     In other words, if we can walk through left child and then right child from the root, we know the target is in the tree.
    def find(self, target: int) -> bool:
        # return target in self.values

        if target == 0:
            return True
        
        values = []
        while target:
            values.append(target)
            target = (target - 1) // 2
        
        node = self.root
        while values:
            value = values.pop()
            if value % 2 == 1 and node.left:
                node = node.left
            elif value % 2 == 0 and node.right:
                node = node.right
            else:
                return False
        
        return True


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)