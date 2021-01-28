def count_nodes(root):
    if root is None:
        return 0
        
    else:
        return 1+count_nodes(root.left) + count_nodes(root.right)

def complete_tree(root,index,nodes):
    if root is None:
        return True
        
    if index>=nodes:
        return False
        
    return (complete_tree(root.left,2*index+1,nodes) and complete_tree(root.right,2*index+2,nodes))
    
        
def checkHeapProperty(root):
    if root.left is None and root.right is None:
        return True
        
    if root.right is None:
        return root.data>=root.left.data
    
    else:
        if(root.data>=root.left.data and root.data>=root.right.data):
            return checkHeapProperty(root.left) and checkHeapProperty(root.right)
            
        else:
            return False
            
            
def isHeap(root):
    
    if root is None:
        return True
        
    node_count = count_nodes(root)
    if complete_tree(root,0,node_count) and checkHeapProperty(root):
        return True
        
    else:
        return False


