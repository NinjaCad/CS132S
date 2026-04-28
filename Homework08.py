class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_child(self):
        return self.right_child or self.left_child

    def has_children(self):
        return self.right_child and self.left_child

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def find_successor(self):
        successor = None
        if self.right_child:
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_child():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.right_child:
                for elem in self.right_child:
                    yield elem
    
    def __str__(self):
        l = self.left_child.key if self.left_child else ""
        r = self.right_child.key if self.right_child else ""
        p = self.parent.key if self.parent else ""
        return f"|K={self.key}|V={self.value}|L={l}|R={r}|P={p}|"

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            inserted_new = self._put(key, value, self.root)
            if inserted_new:
                self.size += 1
        else:
            self.root = TreeNode(key, value)
            self.size += 1

    def _put(self, key, value, current_node):
        if key == current_node.key:
            current_node.value = value
            return False
        
        if key < current_node.key:
            if current_node.left_child:
                return self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                return True
        else:
            if current_node.right_child:
                return self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                return True

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
        return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        if current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return bool(self._get(key, self.root))

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._delete(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")

    def _delete(self, current_node):
        if current_node.is_leaf():  # removing a leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_children():  # removing a node with two children
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:  # removing a node with one child
            if current_node.left_child:
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_value(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_value(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )

    def __delitem__(self, key):
        self.delete(key)
    
    def __str__(self):
        if not self.root:
            return "[]"

        def build_lines(node, indent):
            sp = " " * indent
            if node is None:
                return [f"{sp}[]"]

            lines = [f"{sp}[{node},"]
            lines.extend(build_lines(node.left_child, indent + 2))
            lines.extend(build_lines(node.right_child, indent + 2))
            lines.append(f"{sp}]")
            return lines

        return "\n" + "\n".join(build_lines(self.root, 0))

def main():
    import inspect
    import random
    
    print("*" * 30 + "\nPrinting main() source code:\n" + "*" * 30)
    print(str(inspect.getsource(main)))
    print("*" * 30 + "\nPrinting main() source output:\n" + "*" * 30)

    myTree = BinarySearchTree()

    data = {"CS121P" : "Introduction to Computer Programming",
            "CS132S" : "Data Structures & Algorithms",
            "CS202H" : "Computer Hardware",
            "CS301A" : "Computer Organization & Architecture",
            "CS312N" : "Networking Principles & Architecture",
            "CS321O" : "Operating Systems",
            "CS321P" : "Programming Languages & Systems",
            "CS322E" : "Software Engineering",
            "CS342D" : "Database Management Systems",
            "CS490I" : "Internship",
            "CS492S" : "Senior Seminar",
            "MA253"  : "Discrete Mathematics"
           }
          
    myRandKeyList = list(data.keys())
    random.shuffle(myRandKeyList)

    print("Binary Search Tree Insertion Test:")
    for i in myRandKeyList:
        print(i,end=' ')
        myTree[i] = "".join(word[0] for word in data[i].split())
        
    print("\n\nBinary Search Tree __str__ Test:")
    print(myTree)
    print("\nBinary Search Tree __iter__ Test:")
    for i in myTree.root:
        print(i + ":" + myTree[i])
    
    print("\nBinary Search Tree Duplicate Key Insertion Test:")
    random.shuffle(myRandKeyList)
    for i in myRandKeyList[:2]:
        print(i,end=' ')
        myTree[i] = data[i]

    print("\n\nBinary Search Tree __str__ Test:")
    print(myTree)
    print("\nBinary Search Tree __iter__ Test:")
    for i in myTree.root:
        print(i + ":" + myTree[i])
    
    print("\nBinary Search Tree __delitem__ Test:")
    random.shuffle(myRandKeyList)
    for i in myRandKeyList[:4]:
        print(i,end=' ')
        del myTree[i]

    print("\n\nBinary Search Tree __str__ Test:")
    print(myTree)
    print("\nBinary Search Tree __iter__ Test:")
    for i in myTree.root:
        print(i + ":" + myTree[i])

if __name__ == "__main__":
    main()