class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def add_child(self, data):
        if self.data == data:
            return "This Node Already exists"
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)


    def search(self, val):
        if self.data == val:
            return True
        if val < self.data: 
            self.left.search(val)
        else:
            return False

        if val > self.data:
            self.right.search(val)

        else:
            return False


    def build_tree_method(self, collection):
        for i in collection:
            if self.data == i:
                pass
            if i < self.data:
                if self.left:
                    self.left.add_child(i)
                else:
                    self.left = BinarySearchTree(i)
            if i > self.data:
                if self.right:
                    self.right.add_child(i)
                else:
                    self.right = BinarySearchTree(i)
            
    # All traversals
    def traverse_inorder(self):
        elements = []
        if self.left:
            elements += self.left.traverse_inorder()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.traverse_inorder()
        return elements


    def traverse_postorder(self):
        collection = []
        if self.left:
            collection+= self.left.traverse_postorder()
        if self.right:
            collection+= self.right.traverse_postorder()
        collection.append(self.data)
        return collection


    def traverse_preorder(self):
        collection = []
        collection.append(self.data)
        if self.left:
            collection += self.left.traverse_preorder()
        if self.right:
            collection += self.right.traverse_preorder()
        return collection


    def calculate_sum(self):
        collection = []
        if self.left:
            collection += self.left.traverse_inorder()
        if self.right:
            collection += self.right.traverse_inorder()
        collection.append(self.data)
        return sum(collection)

    def find_max_recur(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max_recur()
    
    
    def find_min_recur(self):
        if self.left is None:
            return self.data
        return self.left.find_min_recur()


    def find_min(self):
        while self.left:
            prev = self.left
            self.left = self.left.left
        return prev.data


    def find_max(self):
        while self.right:
            prev = self.right
            self.right = self.right.right
        return prev.data

    def delete(self, val):
        if self.data is None:
            return None
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
            

if __name__ == "__main__":
    
    arr = [6,3,2,9,12,1,0,8]
    root = BinarySearchTree(7)
    root.build_tree_method(arr)
    # traverse_inorder_iter(root)
    print(root.traverse_inorder())
    print(root.calculate_sum())
    print(root.find_min_recur())
    print(root.find_max_recur())
    root.delete(12)
    print(root.traverse_inorder())

    # binary_tree = build_tree(arr)
    # root = BinarySearchTree(5)
    # root.left = BinarySearchTree(3) 
    # root.left.left = BinarySearchTree(0) 
    # root.left.right = BinarySearchTree(2)  
    # root.right = BinarySearchTree(4)
    # root.right.right = BinarySearchTree(6)
    # root.right.left = BinarySearchTree(5)
    # traverse_inorder_iter(root)