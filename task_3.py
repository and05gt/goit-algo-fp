import heapq


class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = set()

    def add_edge(self, u, v, weight):
        """Adds a directed edge from u to v with the given weight."""

        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
            
        self.edges[u].append((v, weight))
        self.nodes.add(u)
        self.nodes.add(v)

def dijkstra(graph, start_node):
    """Returns the shortest paths using Dijkstra's algorithm."""
    
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start_node] = 0
    
    # Create a pyramid (Priority Queue)
    min_heap = [(0, start_node)]
    
    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)
        
        if current_dist > shortest_paths[current_node]:
            continue
        
        for neighbor, weight in graph.edges.get(current_node, []):
            distance = current_dist + weight
            
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
                
    return shortest_paths

if __name__ == "__main__":
    g = Graph()
    
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)
    g.add_edge('D', 'F', 11)
    g.add_edge('E', 'F', 20)

    start_vertex = 'A'
    
    print(f"Graph created. Find the shortest paths from the vertex '{start_vertex}'...")

    distances = dijkstra(g, start_vertex)

    print("\nResults (Vertex -> Shortest Distance):")
    print("-" * 40)
    
    for vertex in sorted(distances):
        dist = distances[vertex]
        path_str = str(dist) if dist != float('inf') else "Unavailable"
        print(f"To vertex {vertex}: \t{path_str}")
    print("-" * 40)
    