x = '''#.#..
.###.
...#.
###..
#....'''
# x = '''....#
# #..#.
# #.?##
# ..#..
# #....'''

height = 5
width = 5
mid_x = width // 2
mid_y = height // 2
layout = [[char == '#' for char in line] for line in x.splitlines()] # true for bug, false for no bug
layout_list = [layout]

def adj_count(depth, row, col):
  count = 0
  if depth > 0: # if there are outer layouts, outer edges adds outer layout's inner edges
    outer_layout = layout_list[depth - 1]
    count += outer_layout[mid_y - 1][mid_x] if row == 0 else 0 # top
    count += outer_layout[mid_y + 1][mid_x] if row == height - 1 else 0 # bottom
    count += outer_layout[mid_y][mid_x - 1] if col == 0 else 0 # left
    count += outer_layout[mid_y][mid_x + 1] if col == width - 1 else 0 # right
  if depth < len(layout_list) - 1: # if there are inner layouts, inner edges adds inner layout's outer edges
    inner_layout = layout_list[depth + 1]
    count += sum(inner_layout[0]) if row == mid_y - 1 and col == mid_x else 0 # 8
    count += sum(inner_layout[height - 1]) if row == mid_y + 1 and col == mid_x else 0 # 18
    count += sum([line[0] for line in inner_layout]) if row == mid_y and col == mid_x - 1 else 0 # 12
    count += sum([line[width - 1] for line in inner_layout]) if row == mid_y and col == mid_x + 1 else 0 # 14
  count += 1 if row > 0 and layout[row - 1][col] else 0 # up
  count += 1 if row < height - 1 and layout[row + 1][col] else 0 # down
  count += 1 if col > 0 and layout[row][col - 1] else 0 # left
  count += 1 if col < width - 1 and layout[row][col + 1] else 0 # right
  return count

for i in range(200):
  new_layout_list = []
  front = layout_list[0]
  outer_top = front[0]
  outer_bottom = front[height - 1]
  outer_left = [line[0] for line in front]
  outer_right = [line[width - 1] for line in front]
  if any(outer_top + outer_bottom + outer_left + outer_right):
    print(f'outer edges exist')
    # new_layout = [[False for j in range(width)] for i in range(height)]
    # new_layout[mid_y - 1][mid_x] = 1 <= sum(outer_top) <= 2
    # new_layout[mid_y + 1][mid_x] = 1 <= sum(outer_bottom) <= 2
    # new_layout[mid_y][mid_x - 1] = 1 <= sum(outer_left) <= 2
    # new_layout[mid_y][mid_x + 1] = 1 <= sum(outer_right) <= 2
    # new_layout_list.append(new_layout)
    layout_list.insert(0, [[False for j in range(width)] for i in range(height)])
  last = layout_list[-1]
  inner_top = last[mid_y - 1][mid_x]
  inner_bottom = last[mid_y + 1][mid_x]
  inner_left = last[mid_y][mid_x - 1]
  inner_right = last[mid_y][mid_x + 1]
  if any([inner_top, inner_bottom, inner_left, inner_right]):
    print('inner edges exist')
    layout_list.append([[False for j in range(width)] for i in range(height)])
  for depth, layout in enumerate(layout_list):
    new_layout = [[False for j in range(width)] for i in range(height)]
    for j in range(height):
      for k in range(width):
        # print(f'i {i} j {j} adj_count {adj_count(i, j)}')
        if j == mid_y and k == mid_x:
          continue
        new_layout[j][k] = layout[j][k]
        count = adj_count(depth, j, k)
        if layout[j][k] and not(count == 1): # if bug and exactly 1 adj, set as dead
          new_layout[j][k] = False
        elif not layout[j][k] and 1 <= count <= 2: # if space and 1 or 2 adj, set as bug
          new_layout[j][k] = True
    new_layout_list.append(new_layout)
  layout_list = new_layout_list
  print('layout list:')
  print('\n\n'.join('\n'.join(''.join('#' if layout[i][j] else '.' for j in range(width)) for i in range(height)) for layout in layout_list))
print(sum(sum(sum(line) for line in layout) for layout in layout_list))
# print(sum(layout_list))