import sys
input = sys.stdin.readline

def build_preorder(inorder, postorder, in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return []
    
    root = postorder[post_right]
    # Find root index in inorder (linear search)
    root_idx = in_left
    while root_idx <= in_right and inorder[root_idx] != root:
        root_idx += 1
    
    left_count = root_idx - in_left
    
    left_preorder = build_preorder(
        inorder, postorder,
        in_left, root_idx - 1,
        post_left, post_left + left_count - 1
    )
    
    right_preorder = build_preorder(
        inorder, postorder,
        root_idx + 1, in_right,
        post_left + left_count, post_right - 1
    )
    
    return [root] + left_preorder + right_preorder


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

preorder = build_preorder(inorder, postorder, 0, n - 1, 0, n - 1)
print(' '.join(map(str, preorder)))
