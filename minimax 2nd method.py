def minimax(node, depth, is_maximizing_player):
    if isinstance(node, int):
        return node

    
    values = [minimax(child, depth + 1, not is_maximizing_player) for child in node]

    if is_maximizing_player:
        return max(values)
    else:
        return min(values)

# Tree based on the structure in the image
tree = [
    [3, 12, 8],   
    [2, 4, 6],     
    [14, 5, 2]    
]

result = minimax(tree, 0, True)

print("Optimal value at root (A):", result)
