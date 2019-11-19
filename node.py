from copy import copy


class NodeKey():
    def __init__(self, value, name=None):
        self.name = name
        self.value = value

    def __lt__(self, other):
        return self.value < other.value or (self.value == other.value and self.name < other.name)

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return self.value == other.value and self.name == other.name

    def __ne__(self, other):
        return self.value != other.value or self.name != other.name

    def __gt__(self, other):
        return self.value > other.value or (self.value == other.value and self.name > other.name)

    def __ge__(self, other):
        return self > other or self == other

    def __str__(self):
        if self.name is None:
            return str(self.value)
        else:
            return str(self.value) + "," + str(self.name)


class Node():
    def __init__(self, value, name=None):
        self.table = table
        self.key = NodeKey(value, name)
        self.value = value
        self.parent = None
        self.realParent = None
        self.left_child = None
        self.right_child = None
        self.height = 0

    def __str__(self):
        return str(self.key)

    def next(self):
        """ Returns the next Node (next key value larger)
        """
        # If has right child, select, then traverse left all the way down
        if self.right_child is not None:
            node = self.right_child
            while node.left_child is not None:
                node = node.left_child
            return node

        node = self
        # Try to find an ancestor that is a left child, return parent of that
        while node.parent is not None:
            if node.parent.left_child == node:
                return node.parent
            node = node.parent

        # Nothing greater than this
        return None

    def previous(self):
        """ Returns the previous Node (next key value smaller)
        """
        # If has left child, select, then traverse right all the way down
        if self.left_child is not None:
            node = self.left_child
            while node.right_child is not None:
                node = node.right_child
            return node

        node = self
        # Try to find an ancestor that is a right child, return parent of that
        while node.parent is not None:
            if node.parent.right_child == node:
                return node.parent
            node = node.parent

        #  Nothing smaller than this
        return None

    def is_leaf(self):
        """ Return True if Leaf, False Otherwise
        """
        return self.height == 0

    def max_child_height(self):
        """ Return Height Of Tallest Child or -1 if No Children
        """
        if self.left_child and self.right_child:
            # two children
            return max(self.left_child.height, self.right_child.height)
        elif self.left_child is not None and self.right_child is None:
            # one child, on left
            return self.left_child.height
        elif self.left_child is None and self.right_child is not None:
            # one child, on right
            return self.right_child.height
        else:
            # no Children
            return -1

    def weigh(self):
        """ Return How Left or Right Sided the Tree Is
        Positive Number Means Left Side Heavy, Negative Number Means Right Side Heavy
        """
        if self.left_child is None:
            left_height = -1
        else:
            left_height = self.left_child.height

        if self.right_child is None:
            right_height = -1
        else:
            right_height = self.right_child.height

        balance = left_height - right_height
        return balance

    def update_height(self):
        """ Updates Height of This Node and All Ancestor Nodes, As Necessary
        """
        node = self
        while node is not None:
            node.height = node.max_child_height() + 1
            node = node.parent

    def root(self):
        node = self
        while node.parent is not None:
            node = node.parent
        return node

    def balance(self, tree):
        """ Balances node, sets new tree root if appropriate
        Note: If balancing does occur, this node will move to a lower position on the tree
        """
        while self.weigh() < -1 or self.weigh() > 1:
            if self.weigh() < 0:
                # right side heavy
                if self.right_child.weigh() > 0:
                    # right-side left-side heavy
                    self.right_child.rotate_left()
                # right-side right-side heavy
                new_top = self.rotate_right()
            else:
                # left side heavy
                if self.left_child.weigh() < 0:
                    # left-side right-side heavy
                    self.left_child.rotate_right()
                # left-side left-side heavy
                new_top = self.rotate_left()

            if new_top.parent is None:
                tree.root = new_top

    def rotate_right(self):
        assert(self.right_child is not None)
        to_promote = self.right_child
        swapper = to_promote.left_child

        # swap children
        self.right_child = swapper
        to_promote.left_child = self
        new_top = self._swap_parents(to_promote, swapper)
        if swapper is not None:
            swapper.update_height()
        self.update_height()
        return new_top

    def rotate_left(self):
        assert(self.left_child is not None)
        to_promote = self.left_child
        swapper = to_promote.right_child

        # swap children
        self.left_child = swapper
        to_promote.right_child = self
        new_top = self._swap_parents(to_promote, swapper)
        if swapper is not None:
            swapper.update_height()
        self.update_height()
        return new_top

    def _swap_parents(self, promote, swapper):
        """ re-assign parents, returns new top
        """
        promote.parent = self.parent
        self.parent = promote
        if swapper is not None:
            swapper.parent = self

        if promote.parent is not None:
            if promote.parent.right_child == self:
                promote.parent.right_child = promote
            elif promote.parent.left_child == self:
                promote.parent.left_child = promote
        return promote

    def genSuccessors(self):
        def swap(matrix, pos1, pos2):
            x1 = pos1[0]
            y1 = pos1[1]
            x2 = pos2[0]
            y2 = pos2[1]
            matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
            return matrix

        # determine the number of moviments
        copyMatrix = copy(self.table.numebrs)
        childs = []
        line, column = self.table.blankSpace
        if line is 0:
            if column is 0:
                childs.append(swap(copyMatrix, [0, 0], [0, 1]))
                childs.append(swap(copyMatrix, [0, 0], [1, 0]))
            elif column is 1:
                childs.append(swap(copyMatrix, [0, 1], [0, 0]))
                childs.append(swap(copyMatrix, [0, 1], [1, 1]))
                childs.append(swap(copyMatrix, [0, 1], [0, 2]))
            elif column is 2:
                childs.append(swap(copyMatrix, [0, 2], [0, 1]))
                childs.append(swap(copyMatrix, [0, 2], [1, 2]))
                childs.append(swap(copyMatrix, [0, 2], [0, 3]))
            elif column is 3:
                childs.append(swap(copyMatrix, [0, 3], [0, 2]))
                childs.append(swap(copyMatrix, [0, 3], [1, 3]))
        elif line is 1:
            pass

    def h1(self):
        return 16 - self.table.numberOfCorrectPieces
