"""Task 5 - Dijkstra, Bellman-Ford, Floyd-Warshall on the assignment graph."""
import heapq
INF = float("inf")

def dijkstra(vertices, edges, src, trace=True):
    adj = {v: [] for v in vertices}
    for u, v, w in edges: adj[u].append((v, w))
    dist = {v: INF for v in vertices}; pred = {v: None for v in vertices}
    dist[src] = 0; pq = [(0, src)]; done = set()
    while pq:
        d, u = heapq.heappop(pq)                       # EXTRACT_MIN
        if u in done: continue
        done.add(u)
        if trace: print(f"  extract {u} (dist={d})")
        for v, w in adj[u]:
            if v not in done and d + w < dist[v]:      # relaxation
                if trace: print(f"     relax {u}->{v}: {d}+{w}={d+w} < {dist[v]} -> update, pred[{v}]={u}")
                dist[v] = d + w; pred[v] = u; heapq.heappush(pq, (dist[v], v))
            elif trace and v not in done:
                print(f"     relax {u}->{v}: {d}+{w}={d+w} >= {dist[v]} -> no change")
    return dist, pred

def bellman_ford(vertices, edges, src, trace=True):
    dist = {v: INF for v in vertices}; pred = {v: None for v in vertices}; dist[src] = 0
    for k in range(1, len(vertices)):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w; pred[v] = u; changed = True
        if trace: print(f"  pass {k}: {dist}")
        if not changed: break
    for u, v, w in edges:                              # V-th pass: negative-cycle check
        if dist[u] != INF and dist[u] + w < dist[v]:
            return dist, pred, True
    return dist, pred, False

def floyd(vertices, edges):
    D = {i: {j: (0 if i == j else INF) for j in vertices} for i in vertices}
    for u, v, w in edges: D[u][v] = min(D[u][v], w)
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if D[i][k] + D[k][j] < D[i][j]: D[i][j] = D[i][k] + D[k][j]
    return D

if __name__ == "__main__":
    V = ["A", "B", "C", "D", "E"]
    E = [("A","B",4),("A","C",7),("B","C",2),("B","D",6),("C","D",1),("D","E",3),("C","E",8)]
    print("=== Dijkstra from A ===")
    d, p = dijkstra(V, E, "A"); print(" dist:", d); print(" pred:", p)
    print("\n=== Bellman-Ford from A (same graph) ===")
    d, p, neg = bellman_ford(V, E, "A"); print(" dist:", d, " negative cycle:", neg)
    print("\n=== Floyd-Warshall all pairs ===")
    D = floyd(V, E)
    print("     " + " ".join(f"{v:>4}" for v in V))
    for i in V: print(f"{i:>4} " + " ".join(f"{'INF' if D[i][j]==INF else D[i][j]:>4}" for j in V))

    print("\n=== Negative edge: A->B 2, A->C 5, C->B -4 ===")
    V2 = ["A","B","C"]; E2 = [("A","B",2),("A","C",5),("C","B",-4)]
    print(" Dijkstra   :", dijkstra(V2, E2, "A", trace=False)[0], " <- B wrong (true value is 1)")
    d, p, neg = bellman_ford(V2, E2, "A", trace=False)
    print(" BellmanFord:", d, " negative cycle:", neg)

    print("\n=== Negative cycle: A->B 1, B->C -3, C->B 1 ===")
    V3 = ["A","B","C"]; E3 = [("A","B",1),("B","C",-3),("C","B",1)]
    print(" BellmanFord negative cycle detected:", bellman_ford(V3, E3, "A", trace=False)[2])
