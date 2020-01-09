x = '''#.#..
.###.
...#.
###..
#....'''

height = 5
width = 5
layout = [[char == '#' for char in line] for line in x.splitlines()] # true for bug, false for no bug
layout_list = []

def adj_count(row, col):
  count = 0
  count += 1 if row > 0 and layout[row - 1][col] else 0 # up
  count += 1 if row < height - 1 and layout[row + 1][col] else 0 # down
  count += 1 if col > 0 and layout[row][col - 1] else 0 # left
  count += 1 if col < width - 1 and layout[row][col + 1] else 0 # right
  return count

while layout not in layout_list:
  new_layout = [[False for j in range(width)] for i in range(height)]
  for i in range(height):
    for j in range(width):
      # print(f'i {i} j {j} adj_count {adj_count(i, j)}')
      new_layout[i][j] = layout[i][j]
      count = adj_count(i, j)
      if layout[i][j] and not(count == 1): # if bug and exactly 1 adj, set as dead
        new_layout[i][j] = False
      elif not layout[i][j] and (count == 1 or count == 2): # if space and 1 or 2 adj, set as bug
        new_layout[i][j] = True
  layout_list.append(layout)
  layout = new_layout
  print('\n'.join(''.join('#' if layout[i][j] else '.' for j in range(width)) for i in range(height)))
  print()

print('FOUND')
print('\n'.join(''.join('#' if layout[i][j] else '.' for j in range(width)) for i in range(height)))
print(sum(2**i if layout[i//width][i%width] else 0 for i in range(height*width)))
# ans 18375063