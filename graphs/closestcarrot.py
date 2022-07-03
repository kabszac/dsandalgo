from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set([(starting_row, starting_col)])
  queue = deque([(starting_row,starting_col, 0)])
  
  while queue:
    row, col, distance = queue.popleft()
    
    if grid[row][col] == 'C':
      return distance
    
    deltas = [(1,0), (-1,0), (0,1), (0,-1)]
    
    for delta in deltas:
      add_row, add_col = delta
      new_row = row + add_row
      new_col = col + add_col
      row_inbound = 0<= new_row < len(grid)
      col_inbound = 0 <= new_col < len(grid[0])
      pos = (new_row, new_col)
      if row_inbound and col_inbound and grid[new_row][new_col] != 'X'  and pos not in visited:
        queue.append((new_row, new_col, distance+1))
        visited.add(pos)
        
  return -1


  #O(rc) runtime
  #O(rc) space adding to each set
  
    
      
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    
    
    
    
    
    
    
    
    
    
    
    