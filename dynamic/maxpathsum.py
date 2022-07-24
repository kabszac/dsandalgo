def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
  pos = (r,c)
  row_inbound = 0 <= r < len(grid)
  col_inbound = 0 <= c < len(grid[0])
  
  if pos in memo:
    return memo[pos]
  
  if not row_inbound or not col_inbound:
    return 0
  
  if r == len(grid)-1 and c == len(grid[0])-1:
    return grid[r][c]
  
  down = _max_path_sum(grid, r+1, c, memo)
  right = _max_path_sum(grid,r, c+1, memo)
  
  
  memo[pos] =  grid[r][c] + max(down, right)
  return memo[pos]

  

# r = # rows
# c = # columns
# Time: O(r*c)
# Space: O(r*c)

  
  
  
  
  
  
  
  
  
  
  
    
    
    
