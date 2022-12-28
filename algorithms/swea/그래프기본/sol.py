import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())  # 6, 5
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    print(graph)
    '''
    g = [
         [],  # 0
         [4, 3],  # 1
         [3, 5],  # 2
         [],  # 3
         [6],  # 4
         [],  # 5
         [],  # 6
     ]
     '''



