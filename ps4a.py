# Problem Set 4a
# Name:
# Collaborators:
# Time spent:

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = Node(8,
            Node(2,
                Node(1),
                Node(5)),
            Node(10))
tree2 = Node(7,
            Node(2,
                Node(1),
                Node(5,
                    Node(4),
                    Node(6))),
            Node(9,
                Node(8),
                Node(10)))
tree3 = Node(5,
            Node(3,
                Node(2),
                Node(4)),
            Node(14,
                Node(12),
                Node(21,
                    Node(19),
                    Node(26))))


def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    return 1+max(find_tree_height(tree.left),find_tree_height(tree.right)) if tree and (tree.left or tree.right) else 0


def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. compare_func(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 compare_func(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    return not(tree and (tree.left or tree.right)) or all(map(lambda t: (not(t and t.value) or compare_func(t.value, tree.value)) and is_heap(t,compare_func),[tree.left,tree.right]))


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
