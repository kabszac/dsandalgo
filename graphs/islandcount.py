def island_count(grid):
  visited  =set()
  count  = 0
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      if traverse(grid, row, column, visited) == True:
        count += 1
  return count
      
def traverse(grid, r, c, visited):
  row_inbound = 0<= r < len(grid)
  col_inbound = 0 <= c < len(grid[0])
  
  if not row_inbound or not col_inbound:
    return False
  
  if grid[r][c] == 'W':
    return False
  
  pos = (r,c)
  if pos in visited:
    return False
  
  visited.add(pos)
  
  traverse(grid,r-1,c,visited)
  traverse(grid,r+1,c,visited)
  traverse(grid,r,c-1,visited)
  traverse(grid,r,c+1,visited)
  
  return True
  
  
  
  
# O(rc) runtime
#O(rc) space 