#  recursive
def trav(graph, current):
    print(current)

    for neighbor in graph[current]:
        trav(graph, neighbor)


#iterative

def trav(graph, start):
    stack = [start]
    while stack:
        current = stack[-1]
        print(current)
        stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)

#O(n) run and space
