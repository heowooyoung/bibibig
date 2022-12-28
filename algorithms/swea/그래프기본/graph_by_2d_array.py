import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 정점개수, 간선개수
    V, E = map(int, input().split())
    '''
    2차원 배열(2d array)
    graph = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0], 
        [0, 0, 0, 1, 0, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0]
    ]
    '''
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1

    # 시작정점, 끝정점
    S, G = map(int, input().split())

    print(graph)




