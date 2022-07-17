from collections import deque

def best_bridge(grid):
  main_island = None
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      potential_island = traverse_island(grid, r, c, set())
      if len(potential_island) > 0:
        main_island = potential_island
        break
  
  visited = set(main_island)
  queue = deque([ ])
  for pos in main_island:
    r, c = pos
    queue.append((r, c, 0))
  
  while queue:
    row, col, distance = queue.popleft()
    if grid[row][col] == 'L' and (row, col) not in main_island:    
      return distance - 1
    
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col
      neighbor_pos = (neighbor_row, neighbor_col)
      if inbounds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited:
        visited.add(neighbor_pos)
        queue.append((neighbor_row, neighbor_col, distance + 1))
  
def inbounds(grid, row, col):
  row_inbounds = 0 <= row < len(grid)
  col_inbounds = 0 <= col < len(grid[0])
  return row_inbounds and col_inbounds
  
def traverse_island(grid, row, col, visited):
  if not inbounds(grid, row, col) or grid[row][col] == 'W':
    return visited
  
  pos = (row, col)
  if pos in visited:
    return visited
  
  visited.add(pos)
  
  traverse_island(grid, row - 1, col, visited)
  traverse_island(grid, row + 1, col, visited)
  traverse_island(grid, row, col - 1, visited)
  traverse_island(grid, row, col + 1, visited)
  return visited



# r = number of rows
# c = number of columns
# Time: O(rc)
# Space: O(rc)

#mysolution

from collections import deque

def best_bridge(grid):
  first_island = None
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      potential = traversedfs(grid, r, c, set())
      if len(potential) > 0:
        first_island = potential
      
  visited = set(first_island)
  queue = deque([])
  
  for island in first_island:
    r,c = island
    queue.append((r,c,0))
    
    
  while queue:
    row, col, distance = queue.popleft()
    
    if grid[row][col] == 'L' and distance != 0:
      return distance-1
    
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for delta in deltas:
      delta_row, delta_col = delta
      new_row = delta_row + row
      new_col = delta_col + col
      new_pos = (new_row, new_col)
      if inbound(grid, new_row, new_col) and new_pos not in visited:
        queue.append((new_row, new_col, distance+1))
        visited.add(new_pos)
        

      
      
      
      
def inbound(grid, r, c):
  row_inbound = 0 <= r < len(grid)
  col_inbound = 0 <= c < len(grid[0])
  
  return row_inbound and col_inbound
      
def traversedfs(grid, row, col, visited):
  if not inbound(grid, row, col):
    return visited
  
  if grid[row][col] == 'W':
    return visited
  
  pos = (row, col)
  if pos in visited:
    return visited
  
  visited.add(pos)
  
  traversedfs(grid, row-1, col, visited)
  traversedfs(grid, row+1, col, visited)
  traversedfs(grid, row, col-1, visited)
  traversedfs(grid, row, col+1, visited)
  
  return visited


#note
#loop through the grid to find one island first
# we use dfs algo check inbound, not W and not already visited
# we add our first island to our new visited set and also add it tour queue with distance
#perform bfs algo 
# check if the pos is l
# if not traverse more 

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
