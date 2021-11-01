sampleInput = {
    'Users' : {'Desktop', 'Documents', 'Downloads'},
    'Desktop' : {'personal', 'work', 'misc'},
    'Documents' : {'doc1.pdf', 'misc1.docs'},
    'Downloads' : {'file1.zip', 'file2.zip', 'file3.zip'},
}

visited = set()

def dfsEg(visited, sampleInput, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in sampleInput[node]:
            dfsEg(visited, sampleInput, neighbour)

print("Following is the Depth-First Search Implementation")
dfsEg(visited, sampleInput, '3')