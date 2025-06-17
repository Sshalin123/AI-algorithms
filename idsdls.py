tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H', 'I'],
    'D': ['J'],
    'E': ['K', 'L'],
    'F': ['M'],
    'G': [],
    'H': ['N', 'O'],
    'I': [],
    'J': ['P', 'Q'],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': ['R', 'S', 'T'],
    'P': [],
    'Q': ['U'],
    'R': [],
    'S': ['V'],
    'T': [],
    'U': [],
    'V': []
}
def depth_limited_search(node, target, limit, path=None):
    if path is None:
        path = []
    path.append(node)
    if node == target:
        return True, path.copy()
    if limit <= 0:
        path.pop()
        return False, None
    for child in tree.get(node, []):
        found, result_path = depth_limited_search(child, target, limit - 1, path)
        if found:
            return True, result_path
    path.pop()
    return False, None

def iterative_deepening_search(start, target):
    depth = 0
    while True:
        print(f"\nTrying depth limit: {depth}")
        found, path = depth_limited_search(start, target, depth)
        if found:
            print("Found:", target)
            print("Path:", " -> ".join(path))
            return
        depth += 1
        if depth > 100:  
            break
    print("None")


print("Depth-Limited Search")
target_node = 'U'
limit = 5
found, path = depth_limited_search('A', target_node, limit)
if found:
    print(f"Found {target_node} within depth {limit}")
    print("Path:", " -> ".join(path))
else:
    print("None")

print("\nIterative Deepening Search")
iterative_deepening_search('A', target_node)
