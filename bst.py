# bst.py
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================
# Evan McKague
# CS261


class Student:
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        return self.grade < kq.grade

    def __gt__(self, kq):
        return self.grade > kq.grade

    def __eq__(self, kq):
        return self.grade == kq.grade

    def __str__(self):
        return 'Person(name=' + self.name + ', age=' + str(self.grade) + ')'


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key

    def insert(self, data):
        '''
        Compares the data being passed to the current node, if less goes left, if greater or eqaul moves right, until it finds an empty node to insert.
        '''
        # if self.val is less than data
        if self.val > data:
            # if there is already a node on the left
            if self.left:
                # run this function again, with the the left node, and the same data
                return self.left.insert(data)
            # if there not a left node
            else:
                # insert node on the left
                self.left = TreeNode(data)
                return True
        # if self.val is greater than or equal to data
        else:
            # if there is already a node on the right
            if self.right:
                # run this function again, with the the right node, and the same data
                return self.right.insert(data)
            # if there not a right node
            else:
                # insert node on the right
                self.right = TreeNode(data)
                return True


class BST:
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None

        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node
        """
        if not self.root:
            self.root = TreeNode(val)
            return True
        else:
            return self.root.insert(val)

    def in_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform in-order traversal of the tree and return a list of visited nodes
        """
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.in_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for in-order traversal:
        # visit left subtree, store current node value, visit right subtree
        self.in_order_traversal(cur_node.left, visited)
        visited.append(cur_node.val)
        self.in_order_traversal(cur_node.right, visited)
        return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform pre-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        # N L R
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.pre_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for in-order traversal:
        # visit left subtree, store current node value, visit right subtree
        visited.append(cur_node.val)
        self.pre_order_traversal(cur_node.left, visited)
        self.pre_order_traversal(cur_node.right, visited)
        return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        # L R N
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.post_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for in-order traversal:
        # visit left subtree, store current node value, visit right subtree
        self.post_order_traversal(cur_node.left, visited)
        self.post_order_traversal(cur_node.right, visited)
        visited.append(cur_node.val)
        return visited

    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.

        Args:
            kq: query key

        Returns:
            True if kq is in the tree, otherwise False
        """
        visited = self.in_order_traversal(self.root)
        # print(visited)

        if kq in visited:
            return True
        else:
            return False

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """
        if not node.left:
            return node
        else:
            return self.left_child(node.left)

    def remove(self, kq):
        """
        Removes node with key k, if the node exists in the BSTree.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """
        print("removing:", kq)

        # Check if Tree is empty
        if not self.root:
            return False

        # Check if value is in tree, returns false if value is not in tree
        if not self.contains(kq):
            return False

        # if data is in root node
        if self.root.val == (kq):
            # print("removing root node")
            # if root has no children
            if not self.root.left and not self.root.right:
                self.root = None
            # if root has only left child
            elif self.root.left and not self.root.right:
                self.root = self.root.left
            # if root has only right child
            elif self.root.right and not self.root.left:
                self.root = self.root.right
            # if root has two children
            elif self.root.left and self.root.right:
                lmParent = self.root
                lMost = self.root.right
                while lMost.left:
                    lmParent = lMost
                    lMost = lMost.left

                # print("lMost:", lMost.val, "lmParent", lmParent.val)
                # set root value to left most child value
                self.root.val = lMost.val
                # if the node had a right child(can't have left)
                if lMost.right:
                    # print("test")
                    if lMost.val < lmParent.val:
                        lmParent.left = lMost.right
                    else:
                        lmParent.right = lMost.right
                else:
                    if lMost.val < lmParent.val:
                        lmParent.left = None

                    else:
                        lmParent.right = None

            return True

        # Establish pointers
        parent = None
        cur = self.root

        # progress pointers until cur.val == kq
        while cur.val is not kq:
            parent = cur
            if kq < cur.val:
                cur = parent.left
            else:
                cur = parent.right

        # cur should now be pointing to node to remove, and parent points to it's parent(if there is one)

        # if cur has no children
        if not cur.left and not cur.right:
            if kq < parent.val:
                parent.left = None
                return True
            else:
                parent.right = None
                return True

        # cur only has left child
        if cur.left and not cur.right:
            print("parent:", parent, "cur:", cur)
            if kq < parent.val:
                parent.left = cur.left
                return True
            else:
                parent.right = cur.left
                return True

        # cur only has right child
        if not cur.left and cur.right:
            if kq < parent.val:
                parent.left = cur.right
                return True
            else:
                parent.right = cur.right
                return True

        # cur has right and left child
        if cur.left and cur.right:
            lmParent = cur
            lMost = lmParent.right

            # create two new pointers, one to the leftmost child of right subtree, and the other to it's parent
            while lMost.left:
                lmParent = lMost
                lMost = lMost.left

            cur.val == lMost.val
            # check for right child
            if lMost.right:
                if lmParent.val > lMost.val:
                    lmParent.left = lMost.right
                    return True
                elif lmParent.val < lMost.val:
                    lmParent.right = lMost.right
                    return True

            # check for no children
            else:
                if lMost.val < lmParent.val:
                    lmParent.left = None
                    return True
                else:
                    lmParent.right = None
                    return True

    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """
        if not self.root:
            return None
        else:
            return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.

        Returns:
            True if the root was removed, otherwise False
        """
        # checks if tree is empty
        if self.root:
            # makes call to remove root
            self.remove(self.root.val)
            return True
        else:
            return False
