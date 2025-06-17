from collections import deque, defaultdict

# Function to build graph using adjacency list
def build_graph():
    graph = defaultdict(list)
    n = int(input("Enter number of edges: "))
    print("Enter each edge in the format: source destination")
    for i in range(n):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
    return graph

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("\nBFS traversal:")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

# DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        print("\nDFS traversal:")
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Main program
graph = build_graph()
start_node = input("\nEnter the starting node: ")
bfs(graph, start_node)
dfs(graph, start_node)

