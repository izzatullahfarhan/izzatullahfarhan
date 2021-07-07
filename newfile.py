#TUGAS STURKTUR CUACA
#NAMA : Izzatullah Farhan
#NIM : TI 17200016

tanya = 'Y'
while(tanya == 'Y'):
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinaryTree(object):
        def __init__(self, root):
            self.root = Node(root)

        def print_tree(self, traversal_type):
            if traversal_type == "preorder":
                return self.preorder_print(tree.root, "[")
            else:
                print("traversal type " +
                      str(traversal_type),+"is not supported.")
                      
                return False
            
        def preorder_print(self, start, traversal):
            # root+>left+>right
            if start:
                traversal += (str(start.value)+"] [")
                traversal = self.preorder_print(start.left, traversal)
                traversal = self.preorder_print(start.right, traversal)
                
            return traversal

    root = input(str("input akar : "))
    simpan_kiri = input(str("input simpan_kiri : "))
    simpan_kanan = input(str("input simpan_kanan : "))
    ranting_kiri_kiri = input(str("input_kiri_kiri : "))
    ranting_kiri_kanan = input(str("input_kiri_kanan : "))
    ranting_kanan_kiri = input(str("input_kanan_kiri : "))
    ranting_kanan_kanan = input(str("input_kanan_kanan : "))

    tree = BinaryTree (root)
    tree.root.left = Node(simpan_kiri)
    tree.root.right = Node(simpan_kanan)
    tree.root.left.left = Node(ranting_kiri_kiri)
    tree.root.left.right = Node(ranting_kiri_kanan)
    tree.root.right.left = Node(ranting_kanan_kiri)
    tree.root.right.right = Node(ranting_kanan_kanan)
    
    print()
    print(tree.print_tree("preorder"))
    print()
    tanya = input(str("Apakah anda ingin mengulang ? [Y/N] : "))
    print()
    