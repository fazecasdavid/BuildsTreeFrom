import math
from domain import *

#   Builds binary tree from: 

#	From pre-order and in-order
#	From post-order and in-order
#	From pre-order and post-order
#	BTS from Post-order
#	BTS from Pre-order
#	BTS from In-order


# IN-ORDER   LPR
# PRE-ORDER  PLR
# POST-ORDER LRP
def from_in_order_and_pre_order(in_o, pre_o, left, right):
    if left > right:
        return None
    # node -> root node
    node = Node(pre_o[from_in_order_and_pre_order.index])
    # split the nodes in left and right at position "in_index"
    in_index = in_o.index(node.value)
    from_in_order_and_pre_order.index += 1
    node.left = from_in_order_and_pre_order(in_o, pre_o, left, in_index - 1)
    node.right = from_in_order_and_pre_order(in_o, pre_o, in_index + 1, right)
    return node


# IN-ORDER   LPR
# PRE-ORDER  PLR
# POST-ORDER LRP
def from_in_order_and_post_order(in_o, post_o, left, right):
    if left > right:
        return None
    # node -> root node
    node = Node(post_o[from_in_order_and_post_order.index])
    from_in_order_and_post_order.index -= 1
    # # split the nodes in left and right at position "in_index"
    in_index = in_o.index(node.value)
    node.right = from_in_order_and_post_order(in_o, post_o, in_index + 1, right)
    node.left = from_in_order_and_post_order(in_o, post_o, left, in_index - 1)
    return node


# IN-ORDER   LPR
# PRE-ORDER  PLR
# POST-ORDER LRP
# IMPORTANT!!! -> !!! THE TREE MAY NOT BE UNIQUE !!!
def from_pre_order_and_post_order(pre_o, post_o, n1, n2):
    if from_pre_order_and_post_order.index >= len(pre_o) or n1 > n2:
        return None
    # node -> root node
    node = Node(pre_o[from_pre_order_and_post_order.index])
    from_pre_order_and_post_order.index += 1
    if n1 == n2 or from_pre_order_and_post_order.index >= len(pre_o):
        return node
    splitter_index = n2 + 1
    for i in range(n1, n2 + 1):
        if pre_o[from_pre_order_and_post_order.index] == post_o[i]:
            splitter_index = i
            break
    if splitter_index <= n2:
        node.left = from_pre_order_and_post_order(pre_o, post_o, n1, splitter_index)
        node.right = from_pre_order_and_post_order(pre_o, post_o, splitter_index + 1, n2)
    return node


# Recursive function to build a binary search tree from
# its postorder sequence
def construct_BST_from_postorder(postorder, start, end):

    # base case
    if start > end:
        return None

    # Construct the root node of the subtree formed by keys of the
    # postorder sequence in range [start, end]
    node = Node(postorder[end])

    # search the index of last element in current range of postorder
    # sequence which is smaller than the value of root node
    i = end
    while i >= start:
        if postorder[i] < node.value:
            break
        i = i - 1

    # Build right subtree before left subtree since the values are
    # being read from the end of the postorder sequence

    # recursively construct the right subtree
    node.right = construct_BST_from_postorder(postorder, i + 1, end - 1)

    # recursively construct the left subtree
    node.left = construct_BST_from_postorder(postorder, start, i)

    # return current node
    return node


def construct_BST_from_preorder(preorder):

    def bst(l, root, i):
        if i >= len(l) or l[i] > root:
            return None, i
        n = Node(l[i])
        n.left, li = bst(l, l[i], i + 1)
        n.right, ri = bst(l, root, li)
        return n, ri

    return bst(preorder, 'Z', 0)[0]


def construct_BST_from_inorder(inorder, start, end):
    if start > end:
        return None

    # Find index of the maximum element
    # from Binary Tree
    i = inorder.index(max(inorder[start:end+1]))

    # Pick the maximum value and make it root
    root = Node(inorder[i])

    # If this is the only element in
    # inorder[start..end], then return it
    if start == end:
        return root

        # Using index in Inorder traversal,
    # construct left and right subtress
    root.left = construct_BST_from_inorder(inorder, start, i - 1)
    root.right = construct_BST_from_inorder(inorder, i + 1, end)
    return root

def main():
    print("1 -> From pre-order and in-order")
    print("2 -> From post-order and in-order")
    print("3 -> From pre-order and post-order")
    print("4 -> BTS from Post-order")
    print("5 -> BTS from Pre-order")
    print("6 -> BTS from In-order")

    command = input("Input: ")

    if command == "1":
        in_o = input("In-order: ").strip("\n").split(" ")
        pre_o = input("Pre-order: ").strip("\n").split(" ")
        from_in_order_and_pre_order.index = 0
        root = from_in_order_and_pre_order(in_o, pre_o, 0, len(in_o) - 1)
        # print("Post-order: ", end=' ')
        # print_post_order(root)
        print(root)
    elif command == "2":
        in_o = input("In-order: ").strip("\n").split(" ")
        post_o = input("Post-order: ").strip("\n").split(" ")
        from_in_order_and_post_order.index = len(in_o) - 1
        root = from_in_order_and_post_order(in_o, post_o, 0, len(in_o) - 1)
        # print("Pre-order: ", end=' ')
        # print_pre_order(root)
        print(root)
    elif command == '3':
        pre_o = input("Pre-order: ").strip("\n").split(" ")
        post_o = input("Post-order: ").strip("\n").split(" ")
        from_pre_order_and_post_order.index = 0
        root = from_pre_order_and_post_order(pre_o, post_o, 0, len(pre_o) - 1)
        # print("In-order: ", end=' ')
        # print_in_order(root)
        print(root)
    elif command == '4':
        post_o = input("Post-order: ").strip("\n").split(" ")
        root = construct_BST_from_postorder(post_o, 0, len(post_o)-1)
        print(root)
    elif command == '5':
        pre_o = input("Pre-order: ").strip("\n").split(" ")
        root = construct_BST_from_preorder(pre_o)
        print(root)
    elif command == '6':
        pre_o = input("In-order: ").strip("\n").split(" ")
        root = construct_BST_from_inorder(pre_o, 0, len(pre_o)-1)
        print(root)

    print()


if __name__ == '__main__':
    # in-order   = D B F E A C H G
    # pre-order  = A B D E F C G H
    # post-order = D F E B H G C A
    main()
