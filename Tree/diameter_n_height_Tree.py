# Python program to find the diameter of binary tree 
  
# A binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
  
""" 
The function Compute the "height" of a tree. Height is the  
number f nodes along the longest path from the root node  
down to the farthest leaf node. 
"""
def height(node): 
      
    # Base Case : Tree is empty 
    if node is None: 
        return 0 ; 
      
    else:
        if node.left != None:
            left_height = 1+ height(node.left)
        else:
            left_height = 1
        if node.right != None:
            right_height = 1 + height(node.right)
        else:
            right_height = 1

        return max(left_height,right_height)
    #Single line solution for the same problem in one return statement

    # return (1 + max(height(node.left),height(node.right)))    
# Function to get the diamtere of a binary tree 
def diameter(root): 
      
    # Base Case when tree is empty  
    if root is None: 
        return 0; 
  
    # Get the height of left and right sub-trees 
    lheight = height(root.left) 
    rheight = height(root.right) 
  
    # Get the diameter of left and irgh sub-trees 
    ldiameter = diameter(root.left) 
    rdiameter = diameter(root.right) 
  
    # Return max of the following tree: 
    # 1) Diameter of left subtree 
    # 2) Diameter of right subtree 
    # 3) Height of left subtree + height of right subtree +1  
    return max(lheight + rheight + 1, max(ldiameter, rdiameter)) 
      
def inorderTraversal(root,arr):
    if root == None:
        return 
    else:
        inorderTraversal(root.left,arr)
        arr.append(root.data)
        inorderTraversal(root.right,arr)
    return arr
# Driver program to test above functions  

def searchElemt(node,element,queue):
    if node == None:
        return False
    # print(node.data)
    queue.append(node.data)
    if node.data == element:
        return True
   
    if ((node.left != None and searchElemt(node.left,element,queue)) or (node.right != None and searchElemt(node.right,element,queue))):
        return True
        
    queue.pop()
    return False

def lowestCommonAncestor(root,p,q):
    queue_p = []
    queue_q = []
    if (not searchElemt(root,p,queue_p)  or not searchElemt(root,q,queue_q)) :
        return -1
    else:
        print(queue_p)
        print(queue_q)
        i = 0
        while i < len(queue_p) or i < len(queue_q):
            if queue_p[i] == queue_q[i]:
                return queue_p[i-1]
            else:
                i = i+1
        return -1

def getBinarySearhTree(arr):
    if len(arr) == 0:
        return  
    else:
        mid = len(arr)//2
        root = Node(arr[mid])
        root.left =  getBinarySearhTree(arr[0:mid])
        root.right =  getBinarySearhTree(arr[mid+1:len(arr)])
        return root
def checkTreeIsBalanced(root):
    if root == None:
        return -1
    else:
        left_height = checkTreeIsBalanced(root.left)
        if left_height == -9999: 
            return -9999

        right_height = checkTreeIsBalanced(root.right)
        if right_height == -9999 :
            return -9999

        diff = abs(left_height-right_height)
        if diff > 1:
            return -9999
        else:
            return max(left_height,right_height) + 1

def levelOrderTraversalTree(root):
    # len(arr)
    # print(arr)
    arr = []
    if root != None:
        arr.append(root)
        while len(arr) != 0:
            print(arr[0].data,end =" ")
            top_element = arr.pop(0)
            if top_element.left != None:
                arr.append(top_element.left)
            if top_element.right != None:
                arr.append(top_element.right)

def constructBST(arr):
    stack = []
    root = Node(arr[0])
    stack.append(root)
    for i in range(1,len(arr)):
        temp = None
        while len(stack) !=0 and arr[i] > stack[-1].data:
            temp = stack.pop(-1)
            
        if temp  ==  None:
            stack[-1].left = Node(arr[i])
            stack.append(stack[-1].left)
        else:
            temp.right = Node(arr[i])
            stack.append(temp.right)
    return root
""" 
Constructed binary tree is  
            1 
          /   \ 
        2      3 
      /  \     /
    4     5   6
             /
            7
             \
              9 
"""
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6)
root.right.left.left = Node(7)
root.right.left.left.right = Node(9)
print("===Print inorder traversal====")
print(inorderTraversal(root,[]))
print("==============================")
print("level order traversal of a Tree")
print(levelOrderTraversalTree(root))
print("==============================")
print((height(root)))
#print "Diameter of given binary tree is %d" %(diameter(root)) 
print(diameter(root))
#Lowest common Ancestor
print(lowestCommonAncestor(root,2,5))
#Get a binary search Treefor sorted array
root_of_bst = getBinarySearhTree([1,2,3,4,5,6])
print(inorderTraversal(root_of_bst,[]))
if checkTreeIsBalanced(root_of_bst) == -9999:
    print("Tree is not Balnced Tree")
else:
    print("Tree is a Balnced Tree")
if checkTreeIsBalanced(root) == -9999:
    print("Tree is not Balnced Tree")
else:
    print("Tree is a Balnced Tree")
print("*****************************")
print("Construct BST from preorder: ")
bstRoot = constructBST([10,5,1,7,40,50])
print("*****************************")
print(inorderTraversal(bstRoot,[]))
