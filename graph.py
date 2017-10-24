from collections import defaultdict,  deque

visited = [False]*(10**7 + 1)

class Graph:
  
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)
                
def DFS(graph, start, path=[]):
    stack = [start]
    while stack:
        top = stack.pop()
        if not visited[top]:
            visited[top] = True
            path.append(top)
            for i in graph[top]:
                if not visited[i]:  
                    stack.append(i)
    return path
    
def BFS(graph, start, path=[]):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        s = queue.popleft()
        path.append(s)
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return path
    
    
