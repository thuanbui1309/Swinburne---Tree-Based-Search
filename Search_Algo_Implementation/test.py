class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive DFS to find all paths
    def findAllPaths(self, root: TreeNode) -> list:
        result = []
        
        def dfs(node, path):
            if not node:
                return
            
            # Add current node to the path
            path.append(node.val)
            
            # If it's a leaf node, store the path
            if not node.left and not node.right:
                result.append(list(path))  # Make a copy of the current path
            
            # Recursively visit left and right children
            dfs(node.left, path)
            dfs(node.right, path)
            
            # Backtrack by removing the last node
            path.pop()
        
        dfs(root, [])
        return result

    # Iterative DFS to find all paths
    def findAllPathsIterative(self, root: TreeNode) -> list:
        if not root:
            return []
        
        result = []
        stack = [(root, [root.val])]
        
        while stack:
            node, path = stack.pop()
            
            if not node.left and not node.right:
                result.append(path)
            
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            
            if node.left:
                stack.append((node.left, path + [node.left.val]))
        
        return result

# Test function to build a binary tree and test both implementations
def test():
    # Construct the following binary tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(root.val)
    
    # # Instantiate the Solution class
    # sol = Solution()

    # paths = sol.findAllPaths(root)
    # for path in paths:
    #     print(sum(path))
    #     if (sum(path) != 4):
    #         paths.remove(path)

    # print(paths)

# Run the test
test()
