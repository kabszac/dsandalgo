def minimum_island(grid):
  visited = set()
  minimum = 100
  
  for row in range(len(grid)):
    for column in range(len(grid[0])): 
      helper_func = helper(grid, row, column, visited)
      if helper_func < minimum and helper_func > 0:
        minimum = helper_func
  return minimum
    
def helper(grid, r, c, visited):
  
  row_inbound = 0<= r < len(grid)
  col_inbound = 0 <= c < len(grid[0])
  
  if not row_inbound or not col_inbound:
    return 0
  
  if grid[r][c] == 'W':
    return 0
  
  pos = (r,c)
  size = 1
  if pos in visited:
    return 0
  
  visited.add(pos)
  size += helper(grid,r-1,c,visited)
  size += helper(grid,r+1,c,visited)
  size += helper(grid,r,c-1,visited)
  size += helper(grid,r,c+1,visited)
  
  return size
  
  
#O(rc) runtime
#O(rc) space as they are being stored in the set
