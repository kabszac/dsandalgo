def count_paths(grid):
  return _count_paths(grid, 0,0, {})

def _count_paths(grid, r, c, memo):
  pos = (r,c)
  row_inbound = 0 <= r < len(grid) 
  col_inbound = 0 <= c < len(grid[0]) 
  
  if pos in memo:
    return memo[pos]
  
  if not row_inbound or not col_inbound:
    return 0
  
  if grid[r][c] == 'X':
    return 0
  
  if r == len(grid)-1 and c ==len(grid[0])-1:
    return 1
  
  down = _count_paths(grid, r+1, c, memo)
  right = _count_paths(grid, r, c+1, memo)
  
  memo[pos] = down + right
  return memo[pos]



# r = # rows
# c = # columns
# Time: O(r*c)
# Space: O(r*c)


  
  
  
  
  
  
  
  
  
  
  
  