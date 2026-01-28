graph={

    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':[],
    'e':[],
    'f':[]
}
visited=set()

def dfs (graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)

    for i in graph[node]:
        dfs(graph,i,visited)

dfs(graph,'a',visited)