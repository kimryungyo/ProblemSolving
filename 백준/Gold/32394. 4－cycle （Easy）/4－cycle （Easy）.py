def main():
    from itertools import combinations
    from sys import stdin
    input = stdin.readline

    MOD = 10**9 + 7

    number_of_vertices, number_of_edges = map(int, input().split())

    adjacency_list = [[] for _ in range(number_of_vertices)]

    for _ in range(number_of_edges):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    def get_pair_index(u, v, total_vertices):
        if u > v:
            u, v = v, u
        return u * total_vertices - (u * (u + 1)) // 2 + (v - u - 1)

    total_unique_pairs = number_of_vertices * (number_of_vertices - 1) // 2

    common_neighbor_counts = [0] * total_unique_pairs

    for current_vertex in range(number_of_vertices):
        neighbors = adjacency_list[current_vertex]
        
        for neighbor1, neighbor2 in combinations(neighbors, 2):
            pair_idx = get_pair_index(neighbor1, neighbor2, number_of_vertices)
            common_neighbor_counts[pair_idx] += 1

    total_four_cycles = 0
    for count in common_neighbor_counts:
        if count >= 2:
            total_four_cycles += (count * (count - 1)) // 2

    total_four_cycles //= 2

    print(total_four_cycles % MOD)

main()