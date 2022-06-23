from collections import deque

def trav(graph, start):
    queue = deque([start])

    while queue:
        current  = queue[0]
        print(current)
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)

#O(n) space
#O(n) time