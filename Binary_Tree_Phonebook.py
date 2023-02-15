print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")
print("")
my_name = []
def menu():
    print("")
    print("************PHONE BOOK*************")
    print("")

    print(" What do you like to do?: ")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contact")
    print("4. Exit")

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def delete(self, val):
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
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

def new_contacts(my_name):
    Elements = list()
    Elements.append(str(input("Enter your First name: ").upper()))
    Elements.append(str(input("Enter your Last name: ").upper()))
    Elements.append(input("Enter your Address:").upper())
    Elements.append(int(input("Enter your Phone number:")))
    print("Your new add list is", Elements)
    my_name.append(Elements)
    my_name_tree = build_tree(my_name)
    print("")
    for i in range(len(my_name_tree.in_order_traversal())):
        print(my_name_tree.in_order_traversal()[i])

    return my_name