from collections import deque

graph={
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':[],
    'e':[],
    'f':[]
}

def bfs(graph,start):
    visited=set()
    queue=deque()

    visited.add(start)
    queue.append(start)
    while queue:
        node=queue.popleft()
        print(node,end=" ")

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

bfs(graph,'a')