
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if node:
                dfs(node.left)        # 1. Sol
                result.append(node.val)  # 2. Kök
                dfs(node.right)       # 3. Sağ

        dfs(root)
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))
