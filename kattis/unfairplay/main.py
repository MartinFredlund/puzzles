from collections import defaultdict
import sys

sys.setrecursionlimit(200000)


class Edge:
    def __init__(self, to, capacity, flow, reverse_edge_index):
        self.to = to
        self.capacity = capacity
        self.flow = flow
        self.rev = reverse_edge_index


def add_edge(graph, u, v, cap):
    forward = Edge(v, cap, 0, len(graph[v]))
    backward = Edge(u, 0, 0, len(graph[u]))

    graph[u].append(forward)
    graph[v].append(backward)


def bfs(graph, level, s, t):
    level.clear()
    level.update({node: -1 for node in graph})  # Reset levels
    level[s] = 0
    queue = [s]

    while queue:
        u = queue.pop(0)
        for edge in graph[u]:
            if edge.capacity - edge.flow > 0 and level.get(edge.to, -1) < 0:
                level[edge.to] = level[u] + 1
                queue.append(edge.to)
    return level.get(t, -1) >= 0


def dfs(graph, level, u, t, flow, ptr):
    if flow == 0 or u == t:
        return flow

    for i in range(ptr[u], len(graph[u])):
        ptr[u] = i
        edge = graph[u][i]

        if level.get(edge.to, -1) == level[u] + 1 and edge.capacity - edge.flow > 0:
            pushed = dfs(
                graph, level, edge.to, t, min(flow, edge.capacity - edge.flow), ptr
            )

            if pushed > 0:
                edge.flow += pushed

                graph[edge.to][edge.rev].flow -= pushed
                return pushed
    return 0


def dinic_max_flow(graph, s, t):
    max_f = 0
    level = {}

    while bfs(graph, level, s, t):
        ptr = {node: 0 for node in graph}
        while True:
            pushed = dfs(graph, level, s, t, float("inf"), ptr)
            if pushed == 0:
                break
            max_f += pushed
    return max_f


def solve_league(N, M, current_points, matches):
    my_team = N - 1
    results = [None] * M
    matches_to_network = []
    for i in range(M):
        u, v = matches[i]
        u -= 1
        v -= 1
        if u == my_team or v == my_team:
            if u == my_team:
                results[i] = 0
            if v == my_team:
                results[i] = 2
            current_points[my_team] += 2
        else:
            matches_to_network.append((u, v, i))
    my_max_points = current_points[my_team]
    for i in range(N):
        if i == my_team:
            continue
        if current_points[i] >= my_max_points:
            print("NO")
            return

    source = 0
    sink = N + len(matches_to_network) + 2
    graph = defaultdict(list)
    total_points_left = 0

    for idx, (u, v, original_match_index) in enumerate(matches_to_network):
        match_node = N + 1 + idx

        add_edge(graph, source, match_node, 2)
        total_points_left += 2

        add_edge(graph, match_node, u + 1, float("inf"))

        add_edge(graph, match_node, v + 1, float("inf"))
    for i in range(N):
        if i == my_team:
            continue
        allowed_points = (my_max_points - 1) - current_points[i]

        if allowed_points < 0:
            print("NO")
            return

        add_edge(graph, i + 1, sink, allowed_points)

    flow = dinic_max_flow(graph, source, sink)
    if flow != total_points_left:
        print("NO")
    else:
        for idx, (u, v, original_match_index) in enumerate(matches_to_network):
            match_node = N + 1 + idx

            flow_to_u = 0
            flow_to_v = 0

            for edge in graph[match_node]:
                if edge.to == u + 1:
                    flow_to_u = edge.flow
                elif edge.to == v + 1:
                    flow_to_v = edge.flow

            if flow_to_u == 2:
                results[original_match_index] = 0
            elif flow_to_v == 2:
                results[original_match_index] = 2
            else:
                results[original_match_index] = 1
        print(*(results))


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)

    try:
        while True:
            n_str = next(iterator)
            if n_str == "-1":
                break

            N = int(n_str)
            M = int(next(iterator))

            current_points = []
            for _ in range(N):
                current_points.append(int(next(iterator)))

            matches = []
            for _ in range(M):
                matches.append((int(next(iterator)), int(next(iterator))))

            solve_league(N, M, current_points, matches)
    except StopIteration:
        pass


if __name__ == "__main__":
    solve()
