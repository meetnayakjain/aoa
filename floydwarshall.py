INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    
    # Initialize the distance matrix with the graph
    dist = [[0] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    # Update distances by considering all vertices as intermediate vertices
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example Usage
if __name__ == "__main__":
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    shortest_paths = floyd_warshall(graph)

    print("Shortest Paths between all pairs:")
    for row in shortest_paths:
        print(row)
