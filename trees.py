import math

#   Builds binary tree from: 

#	From pre-order and in-order
#	From post-order and in-order
#	From pre-order and post-order
#	BTS from Post-order
#	BTS from Pre-order
#	BTS from In-order

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))


def _build_tree_string(root, curr_index, index=False, delimiter='-'):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
    else:
        node_repr = str(root.value)

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        _build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        _build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


# IN-ORDER   LPR
def print_in_order(root):
    if root is not None:
        print_in_order(root.left)
        print(root.value, end=' ')
        print_in_order(root.right)


# PRE-ORDER  PLR
def print_pre_order(root):
    if root is not None:
        print(root.value, end=' ')
        print_pre_order(root.left)
        print_pre_order(root.right)


# POST-ORDER LRP
def print_post_order(root):
    if root is not None:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.value, end=' ')


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
def constructBST(postorder, start, end):

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
    node.right = constructBST(postorder, i + 1, end - 1)

    # recursively construct the left subtree
    node.left = constructBST(postorder, start, i)

    # return current node
    return node


def bstFromPreorder(preorder):

    def bst(l, root, i):
        if i >= len(l) or l[i] > root:
            return None, i
        n = Node(l[i])
        n.left, li = bst(l, l[i], i + 1)
        n.right, ri = bst(l, root, li)
        return n, ri

    return bst(preorder, 'Z', 0)[0]


def buildTree(inorder, start, end):
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
    root.left = buildTree(inorder, start, i - 1)
    root.right = buildTree(inorder, i + 1, end)
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
        root = constructBST(post_o, 0, len(post_o)-1)
        print(root)
    elif command == '5':
        pre_o = input("Pre-order: ").strip("\n").split(" ")
        root = bstFromPreorder(pre_o)
        print(root)
    elif command == '6':
        pre_o = input("In-order: ").strip("\n").split(" ")
        root = buildTree(pre_o, 0, len(pre_o)-1)
        print(root)

    print()


if __name__ == '__main__':
    # in-order   = D B F E A C H G
    # pre-order  = A B D E F C G H
    # post-order = D F E B H G C A
    main()
