import sys
input = sys.stdin.readline

def build_postorder(inorder, preorder, in_left, in_right, pre_idx):
    if in_left > in_right:
        return [], pre_idx
    
    root = preorder[pre_idx]
    pre_idx += 1

    # Find root index by scanning inorder segment
    root_idx = in_left
    while root_idx <= in_right and inorder[root_idx] != root:
        root_idx += 1

    left_part, pre_idx = build_postorder(inorder, preorder, in_left, root_idx - 1, pre_idx)
    right_part, pre_idx = build_postorder(inorder, preorder, root_idx + 1, in_right, pre_idx)

    return left_part + right_part + [root], pre_idx


n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

postorder, _ = build_postorder(inorder, preorder, 0, n - 1, 0)
print(' '.join(map(str, postorder)))
