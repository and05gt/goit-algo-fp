import collections
import colorsys
from task_4 import Node, draw_tree

def generate_color_gradient(n_steps, step_index):
    """Generates a HEX color from dark blue to light."""

    hue = 0.6
    saturation = 0.8

    if n_steps > 1:
        luminance = 0.3 + (0.65 * step_index) / (n_steps - 1)
    else:
        luminance = 0.65

    rgb = colorsys.hls_to_rgb(hue, luminance, saturation)

    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

def count_nodes(node):
    """Counts the total number of nodes in the tree."""

    if node is None:
        return 0
    
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def visualize_bfs(root):
    """Visualizes the tree using BFS"""

    if root is None:
        return
    
    total_nodes = count_nodes(root)
    queue = collections.deque([root])
    step = 0

    while queue:
        # Queue: FIFO (First In, First Out)
        node = queue.popleft()

        hex_color = generate_color_gradient(total_nodes, step)
        node.color = hex_color

        step += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    draw_tree(root)

def visualize_dfs(root):
    """Visualizes the tree using DFS"""

    if root is None:
        return
    
    total_nodes = count_nodes(root)
    stack = [root]
    step = 0

    while stack:
        # Stack: LIFO (Last In, First Out)
        node = stack.pop()

        hex_color = generate_color_gradient(total_nodes, step)
        node.color = hex_color

        step += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    draw_tree(root)

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(8)

    # Running BFS
    print("Visualizing BFS...")
    visualize_bfs(root)

    # Running DFS
    print("Visualizing DFS...")
    visualize_dfs(root)
