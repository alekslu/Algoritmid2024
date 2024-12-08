# Kirja pandud ja selgeks tehtud internetis leiduva materjali toel. 

class Node:
    def __init__(self, key):
        self.left = None  # Vasakpoolne laps (alguses tühi)
        self.right = None  # Parempoolne laps (alguses tühi)
        self.val = key  # Sõlme väärtus

    # Eelnev läbimine (Pre-order). Liikumise järjekord: sõlm, vasak, parem
    def traversePreOrder(self):
        print(self.val, end=' ')  # Print hetke sõlme väärtus
        if self.left:  # Kui vasak laps, siis mine vasakule
            self.left.traversePreOrder()
        if self.right:  # Kui parem laps, mine paremale
            self.right.traversePreOrder()

    # Sisemine läbimine (In-order). Liikumise järjekord: vasak, sõlm, parem
    def traverseInOrder(self):
        if self.left:  
            self.left.traverseInOrder()
        print(self.val, end=' ')  
        if self.right:  
            self.right.traverseInOrder()

    # Pärast juurt läbimine (Post-order). Liikumise järjekord:vasak, parem, sõlm
    def traversePostOrder(self):
        if self.left: 
            self.left.traversePostOrder()
        if self.right:  
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node(1)  # Juur
root.left = Node(2)  # Juure vasak child
root.right = Node(3)  # Juure parem child
root.left.left = Node(4)  # Juure vasaku lapse laps

# Eelnev läbimine
print("Pre order Traversal: ") 
root.traversePreOrder()  # Trüki sõlmed eelnevas järjekorras
print("\nIn order Traversal: ")
root.traverseInOrder()  # Trüki sõlmed sisemises järjekorras
print("\nPost order Traversal: ")
root.traversePostOrder()  # Trüki sõlmed pärast juurt järjekorras
