from random import *
from time import *
import csv

class Node():
    def __init__(self, digit):
        self.digit = digit
        self.left = None
        self.right = None
        self.perent = None

def insert_in_tree(root, unit):
    if root is None:
        root = unit
    else:
        if root.digit > unit.digit:
            if root.left is None:
                root.left = unit
            else:
                insert_in_tree(root.left, unit)
        elif root.digit < unit.digit:
            if root.right is None:
                root.right = unit
            else:
                insert_in_tree(root.right, unit)
                
def sort_max(root):
    if root != None:
        sort_max(root.left)
        # print(root.digit)
        sort_max(root.right)


if __name__=="__main__":
    
    finall_array = []
    result = []
    cycle_quality = 10000
    
    tree = Node(randint(1, cycle_quality))
    
    """TEST FIRST. WITH USING TREE SORT"""
    start = time()
    
    for cycle in range(cycle_quality):
        insert_in_tree(tree, Node(randint(1, cycle_quality)))
    sort_max(tree)
    
    stop = time()
    difference = stop-start
    result.append(["Tree sort", difference])
    
    """TEST SECOND. WITH USING STANDART SORT"""
    start = time()
    
    for cycle in range(cycle_quality):
        finall_array.append(randint(1, cycle_quality))
    finall_array.sort()
    # for cycle in range(cycle_quality):
    #     print(finall_array[cycle])
    
    stop = time()
    difference = stop-start
    result.append(["Standart sort", difference])
    
    """RESULT"""
    with open("data.csv", "r", encoding='UTF-8') as file:
        reader = csv.reader(file)
        
        result.append([])#add indent
        
        for object_in_file in reader:
            result.append(object_in_file)
            

    with open('data.csv', "w", newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        for i in result:
            writer.writerow(i)
        
        
    #print(f'\n\nTree sort 1 - \t{result}\nsort() 2 - \t{result2}\n\n')