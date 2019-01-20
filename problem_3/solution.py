class Tree:

    def __init__(self, root=None):
        self.root = root

    # def add_node(self, node, current_node=None):
    #     if self.root is None:
    #         self.root = node
    #         return
    #     if current_node is None:
    #         current_node = self.root
    #     if node.val == current_node.val:
    #         return
    #     elif node.val < current_node.val:
    #         if current_node.left is None:
    #             current_node.left = node
    #         else:
    #             self.add_node(node, current_node=current_node.left)
    #     elif node.val > current_node.val:
    #         if current_node.right is None:
    #             current_node.right = node
    #         else:
    #             self.add_node(node, current_node=current_node.right)

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    result = ''

    result += node.val

    result += ','
    result += '{'

    if node.left is not None:
        result += serialize(node.left) 

    result += '}'
    result += ','
    result += '{'

    if node.right is not None:
        result += serialize(node.right)

    result += '}'

    return result

def deserialize(string):
    if string == '{}' or string == '':
        return None

    val = None
    left_begins_at = None

    for index, char in enumerate(string):
        if char == ',':
            val = string[:index]
            left_begins_at = index + 1
            break

    open_brackets = 0
    close_brackets = 0
    left_ends_at = None
    for index, char in enumerate(string[left_begins_at:]):
        if char == '{':
            open_brackets += 1
        elif char == '}':
            close_brackets += 1
        if open_brackets != 0 and close_brackets != 0 and open_brackets == close_brackets:
            left_ends_at = index + left_begins_at
            break

    open_brackets = 0
    close_brackets = 0
    right_begins_at = left_ends_at + 2
    right_ends_at = None
    for index, char in enumerate(string[right_begins_at:]):
        if char == '{':
            open_brackets += 1
        elif char == '}':
            close_brackets += 1

        if open_brackets != 0 and close_brackets != 0 and open_brackets == close_brackets:
            right_ends_at = index + right_begins_at
            break

    node = Node(val)

    node.left = deserialize(string[left_begins_at + 1:left_ends_at])
    node.right = deserialize(string[right_begins_at + 1:right_ends_at])

    return node


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    success = deserialize(serialize(node)).left.left.val == 'left.left'
    print("Deserialization and serialization work:", success)
    assert success