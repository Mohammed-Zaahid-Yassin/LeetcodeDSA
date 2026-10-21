class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def inorder(node: TreeNode | None) -> None:
            if node is None:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result
