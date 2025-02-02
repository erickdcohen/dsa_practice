"""
General tree implementation example using products
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = "  " * self.get_level() * 2 
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def main():
    root = TreeNode("electronics")

    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("thinkpad"))

    cellphone = TreeNode("cellphone")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("pixel"))
    cellphone.add_child(TreeNode("samsung"))

    tv = TreeNode("tv")
    tv.add_child(TreeNode("lg"))
    tv.add_child(TreeNode("toshiba"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

    return root

if __name__ == "__main__":
    main()
