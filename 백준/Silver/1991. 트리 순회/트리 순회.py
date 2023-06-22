preorder, inorder, postorder = '', '', ''
N = int(input())
tree = {}
for _ in range(N):
    A, B, C = input().split()
    tree[A] = [B, C]

def preorder_tree(T):
    global preorder
    if T != '.':
        preorder += T
        preorder_tree(tree[T][0])
        preorder_tree(tree[T][1])

def inorder_tree(T):
    global inorder
    if T != '.':
        inorder_tree(tree[T][0])
        inorder += T
        inorder_tree(tree[T][1])

def postorder_tree(T):
    global postorder
    if T != '.':
        postorder_tree(tree[T][0])
        postorder_tree(tree[T][1])
        postorder += T

preorder_tree('A')
inorder_tree('A')
postorder_tree('A')

print(preorder)
print(inorder)
print(postorder)