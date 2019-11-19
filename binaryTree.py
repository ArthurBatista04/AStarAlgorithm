import random
import math
from node import Node


class BinaryTree():
    """ Binary Search Tree
    Uses AVL Tree
    """

    def __init__(self, *args):
        self.root = None  # root Node
        self.element_count = 0
        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def __len__(self):
        return self.element_count

    def __str__(self):
        return self.out()

    def height(self):
        """ Return Max Height Of Tree
        """
        if self.root:
            return self.root.height
        else:
            return 0

    def balance(self):
        """ Perform balancing Operation
        """
        if self.root is not None:
            self.root.balance(self)

    def insert(self, value, name=None):
        if self.root is None:
            # If nothing in tree
            self.root = Node(value, name)
        else:
            if self.find(value, name) is None:
                # If key/name pair doesn't exist in tree
                self.element_count += 1
                self.add_as_child(self.root, Node(value, name))

    def add_as_child(self, parent_node, child_node):
        if child_node.key < parent_node.key:
            # should go on left
            if parent_node.left_child is None:
                # can add to this node
                parent_node.left_child = child_node
                child_node.parent = parent_node
                child_node.update_height()
            else:
                self.add_as_child(parent_node.left_child, child_node)
        else:
            # should go on right
            if parent_node.right_child is None:
                # can add to this node
                parent_node.right_child = child_node
                child_node.parent = parent_node
                child_node.update_height()
            else:
                self.add_as_child(parent_node.right_child, child_node)

        if parent_node.weigh() not in [-1, 0, 1]:
            parent_node.balance(self)

    def inorder_non_recursive(self):
        node = self.root
        retlst = []
        while node.left_child:
            node = node.left_child
        while node:
            if node.key.name is not None:
                retlst.append([node.key.value, node.key.name])
            else:
                retlst.append(node.key.value)
            if node.right_child:
                node = node.right_child
                while node.left_child:
                    node = node.left_child
            else:
                while node.parent and (node == node.parent.right_child):
                    node = node.parent
                node = node.parent
        return retlst

    def preorder(self, node, retlst=None):
        if retlst is None:
            retlst = []
        if node.key.name is not None:
            retlst.append([node.key.value, node.key.name])
        else:
            retlst.append(node.key.value)
        if node.left_child:
            retlst = self.preorder(node.left_child, retlst)
        if node.right_child:
            retlst = self.preorder(node.right_child, retlst)
        return retlst

    def inorder(self, node, retlst=None):
        if retlst is None:
            retlst = []
        if node.left_child:
            retlst = self.inorder(node.left_child, retlst)
        if node.key.name is not None:
            retlst.append([node.key.value, node.key.name])
        else:
            retlst.append(node.key.value)
        if node.right_child:
            retlst = self.inorder(node.right_child, retlst)
        return retlst

    def postorder(self, node, retlst=None):
        if retlst is None:
            retlst = []
        if node.left_child:
            retlst = self.postorder(node.left_child, retlst)
        if node.right_child:
            retlst = self.postorder(node.right_child, retlst)
        if node.key.name is not None:
            retlst.append([node.key.value, node.key.name])
        else:
            retlst.append(node.key.value)
        return retlst

    def as_list(self, pre_in_post):
        if not self.root:
            return []
        if pre_in_post == 0:
            return self.preorder(self.root)
        elif pre_in_post == 1:
            return self.inorder(self.root)
        elif pre_in_post == 2:
            return self.postorder(self.root)
        elif pre_in_post == 3:
            return self.inorder_non_recursive()

    def find(self, value, name=None):
        return self.find_in_subtree(self.root, NodeKey(value, name))

    def find_in_subtree(self, node, node_key):
        if node is None:
            return None  # key not found
        if node_key < node.key:
            return self.find_in_subtree(node.left_child, node_key)
        elif node_key > node.key:
            return self.find_in_subtree(node.right_child, node_key)
        else:  # key is equal to node key
            return node

    def remove(self, key):
        # first find
        node = self.find(key)

        if not node is None:
            self.element_count -= 1

            if node.is_leaf():
                # The node is a leaf.  Remove it and return.
                self.remove_leaf(node)
            elif (node.left_child is not None and node.right_child is None) or (node.left_child is None and node.right_child is not None):
                # The node has only 1 child. Make the pointer to this node point to the child of this node.
                self.remove_branch(node)
            else:
                # The node has 2 children. Swap items with the successor (the smallest item in its right subtree) and
                # delete the successor from the right subtree of the node.
                assert node.left_child and node.right_child
                self.swap_with_successor_and_remove(node)

    def remove_leaf(self, node):
        parent = node.parent
        if parent:
            if parent.left_child == node:
                parent.left_child = None
            else:
                assert (parent.right_child == node)
                parent.right_child = None
            parent.update_height()
        else:
            self.root = None

        # rebalance
        node = parent
        while node:
            if not node.weigh() in [-1, 0, 1]:
                node.balance(self)
            node = node.parent

    def remove_branch(self, node):
        parent = node.parent
        if parent:
            if parent.left_child == node:
                parent.left_child = node.right_child or node.left_child
            else:
                assert (parent.right_child == node)
                parent.right_child = node.right_child or node.left_child

            if node.left_child:
                node.left_child.parent = parent
            else:
                assert node.right_child
                node.right_child.parent = parent
            parent.update_height()

        # rebalance
        node = parent
        while node:
            if not node.weigh() in [-1, 0, 1]:
                node.balance(self)
            node = node.parent

    def swap_with_successor_and_remove(self, node):
        successor = node.right_child
        while successor.left_child:
            successor = successor.left_child
        self.swap_nodes(node, successor)
        assert (node.left_child is None)
        if node.height == 0:
            self.remove_leaf(node)
        else:
            self.remove_branch(node)

    def swap_nodes(self, node_1, node_2):
        assert (node_1.height > node_2.height)
        parent_1 = node_1.parent
        left_child_1 = node_1.left_child
        right_child_1 = node_1.right_child
        parent_2 = node_2.parent
        assert (not parent_2 is None)
        assert (parent_2.left_child == node_2 or parent_2 == node_1)
        left_child_2 = node_2.left_child
        assert (left_child_2 is None)
        right_child_2 = node_2.right_child

        # swap heights
        tmp = node_1.height
        node_1.height = node_2.height
        node_2.height = tmp

        if parent_1:
            if parent_1.left_child == node_1:
                parent_1.left_child = node_2
            else:
                assert (parent_1.right_child == node_1)
                parent_1.right_child = node_2
            node_2.parent = parent_1
        else:
            self.root = node_2
            node_2.parent = None

        node_2.left_child = left_child_1
        left_child_1.parent = node_2
        node_1.left_child = left_child_2  # None
        node_1.right_child = right_child_2
        if right_child_2:
            right_child_2.parent = node_1
        if not (parent_2 == node_1):
            node_2.right_child = right_child_1
            right_child_1.parent = node_2

            parent_2.left_child = node_1
            node_1.parent = parent_2
        else:
            node_2.right_child = node_1
            node_1.parent = node_2

            # use for debug only and only with small trees

    def out(self, start_node=None):
        if start_node is None:
            start_node = self.root

        if start_node is None:
            return None
        else:
            return start_node.out()
