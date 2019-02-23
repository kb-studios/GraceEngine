from anytree import Node, RenderTree, AsciiStyle
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
import json

class Trie:

    def showTree(node):
        print(RenderTree(node, style=AsciiStyle()).by_attr())
        
    
    def traverseTree(node, cmd:list, length:int, cnt:int):
        
        '''
            This function receives a tree and the instruction and then executes the command
            If it has to work with json, first convert it into a tree using import.read(filehandle)
        '''


        '''Split the input commands and check each keyword hierarchically'''
        key = cmd[cnt]
        
        for child in node.children:
            if child.name == key:
                if cnt == length-1:
                    if child.isLeaf == True:
                        # TODO : function call or assign an id to execute the code
                        print("Execute the corresponding code")
                        return
                Trie.traverseTree(child, cmd, length, cnt+1)


    def addNode(node, cmd:str, cnt:int, init:int):
        key = cmd[init]
        flag = 0
        for child in node.children:
            if child.name == key:
                flag = 1
                if init != cnt-1:
                    Trie.addNode(child,cmd,cnt,init+1)
                else:
                    print("Node already exists")
                    return
        if flag == 0:
            newNode = Node(key, parent=node, isLeaf=True)
            # TODO: find a way to assign True to isLeaf for correct nodes
            if init != cnt-1:
                Trie.addNode(newNode,cmd,cnt,init+1)


    '''Convert the given tree into json'''
    def toJson(root):
        exporter = JsonExporter(indent=2, sort_keys=False)
        print(exporter.export(root))

        with open('trie.json','w') as f:
            exporter.write(root,f)

if __name__ == '__main__':
    _ = Trie()
    root = Node("*")

    query = "create array integers"
    query = query.split(' ')
    Trie.addNode(root,query,len(query),0)


    query = "create array integers"
    query = query.split(' ')
    Trie.addNode(root,query,len(query),0)


    query = "create list integers"
    query = query.split(' ')
    Trie.addNode(root,query,len(query),0)


    query = "repeat while"
    query = query.split(' ')
    Trie.addNode(root,query,len(query),0)

    query = "repeat while"
    query = query.split(' ')
    Trie.traverseTree(root,query,len(query),0)

    Trie.showTree(root)