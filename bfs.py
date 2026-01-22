from collections import deque

def bfs(graph,start):
    visited=set()
    queue=deque()

    visited.add(start)
    queue.append(start)
    while queue:
        node=queue.popleft()
        print(node,end=" ")

        for nabiuger in graph[node]:
            if nabiuger not in visited:
                visited.add(nabiuger)
                queue.append(nabiuger)

graph={
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':[],
    'e':[],
    'f':[]
}

bfs(graph,'a')