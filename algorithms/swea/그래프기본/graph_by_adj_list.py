import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 정점개수, 간선개수
    V, E = map(int, input().split())

    '''
    인접리스트 (Adj list)
    graph = [           idx == 정점 번호
         [],            # 0
         [4, 3],        # 1
         [3, 5],        # 2
         [],            # 3
         [6],           # 4
         [],            # 5
         [],            # 6
     ]
     '''
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    # 시작정점, 끝정점
    S, G = map(int, input().split())

    print(graph)




