import timeit # for benchmarking

maze = '''#################################################################################
#.#.........#........s..#...#...........#.#z..#.........#...#................e..#
#.#.#######.#.###.#####.#.#.#########.#.#.#.#.#.#.#######.#.#.###########.#####.#
#...#.....#.#...#.#...#.#.#.....#.....#.#.#.#.#.#.........#....f#.......#.#.....#
#.#######.#.#.###.#.###.#.#####.#.#####.#.#.#.#.#########.#######.#####.###.###C#
#.#.......#.#.#...#...#...#...#.#...#.#.#...#.R...#.....#.#...#...#.........#...#
#.#.#######.#.#.###.#.#####.#.#.###.#.#.#.#####.###.###.#.#.#.#.#.###########.###
#.#.#.....#...#.#...#.....#.#.#...#.#...#.#...#.#...#...#...#.#.#.#.......#...#.#
#.#.#.###.#.###.#.#####.#.###.###.#.#######.#.###.###.#########.###.#####.#.###.#
#...#.#...#.#...#.#...#.#.....#...#.....#...#...#.#.#u........#j..#.#.#...#.....#
#.###.#.#####.###.###.#.###.###.###.###.#.#####.#.#.#########.#.#P#.#.#.#######.#
#.#...#...#...#.......#.#...#...#.....#.#...#...#x#.....#.....#.#.....#...Y.#...#
#.#.#####.#.###.#######.#.###.#########.###.#.###.#####.#.#####.###########.#.###
#.#...#.....#...#.....#.#.#.#.#.........#...#.#.....#...#..g..#.#.#.........#...#
#####.#######.###.###.#.#.#.#.###.#####.#.###.#####.#.#######.#.#.#.###########.#
#...#.#...#.#.#.#...#...#...#...#.#...#.#...#.....#.#.....#...#...#.Q.....#.....#
#.#.#.#.#.#.#.#.###.#######.###.#.###.#.#.#.#####.#.#.###.#.#########.###.#.#####
#.#.W.#.#.#.#...#...#...#.#.#.#.#...#...#.#.#.......#...#m..........#...#.#.#...#
#.#####.#.#.###.#.###.#.#.#.#.#.###.#.###.#.#######################.###.#.#.###.#
#.#.....#.#.....#.#...#.#.....#.#...#...#.#.#.......#...#.......#...#...#.#.#...#
#.#.#####.#.#####.#.###.#.#####.#.#####.#.#.#.#####.#.#.#.#####.###.#####.#.#.###
#k#.#...#.#...V.#...#.#.#...#...#.#...#.#.#...#...#...#...#...#...#.......#.#...#
#.#.#.###.#####.#####.#.#####.###.#.#.#.#.#####.#.#########.#####.#########.###.#
#.....#.N.#...#...#...#.....#.....#.#...#.#.....#.#...#.....#.....#.....#.......#
#######.#.#.#.###.#.#######.#######.#####.###.###.#.#.#.#####.#.###.###.#.#######
#.......#.#.#.#.#.#...#...#.........#...#.....#...#.#...#.....#.......#.#...#...#
#.###.#####.#.#.#.###.#.#.#######.#####.#######.###.#################.#.#####.#D#
#.#.#.#.....#.#.#...#...#.......#.B...#.#.....#...#.#...............#.#..v..#.#.#
#.#.#.#.#####.#.###.###########.#####.#.###.#.###.#.#####.#########.#.#####.#.#.#
#.#...#.#...#.#.....#.......#...#...#.#.#...#.#...#.#...#.#...#.#...#.....#...#.#
#.#.###.###.#.###.#####.#.###.###.###.#.#.###.#.###.#.#.#.#.#.#.#.#############.#
#.#...#.#...#...#.#...#.#.#...#...#...#.#.#...#.#...#.#...#.#...#.#.......#...#.#
#.#####.#.#####.#.#.#.#.###.###.#.#.###.#.#####.#.###.#####.#####.#.#####.#.#.#.#
#.......#.....#.#...#.#.#...#...#.#...#.#.......#.#.....#.......#...#...#...#.#.#
#.#########.###.#####.#.#.###.###.###.#.#.#######.###.#.#.#####.#####.#.#####.#.#
#...........#...#...#...#...#.#.....#...#.......#...#.#.#.....#...#...#...#...#.#
###########.#.###.#.#.#####.#.#.#######.###########.###.#####.###.#.#.#####.###.#
#...#...#...#.#...#.#.#.....#.#.#.....#.#...........#...#...#...#...#.#...#.#.I.#
#.###.#.#.###.#.###.###.#####.###.#.###.#.###########.###.#####.#####.#.#.#.#.#.#
#.....#.....#.....#.....#.........#...................#.............#...#.....#.#
#######################################.@.#######################################
#...#d..#.....#.....#.......#.....#.#.................#.............A.#.........#
#.#.###.#.#.###L###.#.#.###.#.###.#.#.#.#.###########.#.#.#############.###.###.#
#.#...#...#...#.#t#.#.#...#a..#...#...#.#.#...#.....#.#.#.....#....l#.....#...#.#
#.###.###.###.#.#.#.#.###.#####.#######.#.#.#.#####.#.#.#####.#.###.#.#######.#.#
#.#.#o..#.#..i#...#...#.#.#.........#...#...#.......#...#...#.#.#.#...#.#.T.#.#.#
#.#.###.#.#.#####.#####.#.#########.#.#.###########.#######.#.#.#.#####.#.#.#.#.#
#.#...#.#.#.....#...#...#.#...#.......#.#...#.......#.......#...#.......#.#...#.#
#.#H###.#######.###.###.#.#.#.#########.###.#.#######.###.#########.###.#.#####.#
#.#.....#.....#.........#...#.....#b....#...#.....#.#.#.#.........#.#...#.....#.#
#.###.###.###.###################.###.###.#######.#.#.#.#######.#.#.#########.###
#...#.....#.#...#...#...........#...#...#...#.....#.#...#.....#.#...#.......#...#
#.#.#######.###.#.#.#.#########.###.#######.#.#####.###.#.#.###.#.###.#####.#.#.#
#.#.#...#...#...#.#...#.......#...#.....#...#...#.....#...#.#...#.#...#...#.#.#.#
#.#.#.#.#.#.#.###.#####.#########.###.#.#.#####.#.#.#######.#.###.#.###.#.#.###.#
#.#.#.#...#.......#.................#.#.#.......#.#.........#...#.#.#.#.#.#...#.#
#.#.#.#########.#########.#########.###.#.#########.###########.#.#.#.#.#.###.#.#
#.#.#.#.......#.#...#...#.#.......#...#.#.#.......#.#...#.......#.#.#.#.#.....#.#
###.#.#.#####.#.#.#.#.#.#.#E#####.###.#.#.#.###.#.#.#.#.#.#########.#.#.#######.#
#...#.#.#...#.#.#.#...#.#.#.#.....#...#.#.#.#...#.#...#.#...#.......#.#.#.....#.#
#.###.#.#.###.#.#.#####.###.#.#####.###.#.#.#.###.#####.###.#.#######.#.###.#.#.#
#.#...#.#...#.#.#.#...#...#.#...#.......#.#.#.#.#.#...#.#...#.#.......#.....#...#
#.###.#.#.#.#.#.#Z#.#####.#.###.#######.#.###.#.#.#.#.#.#.#####.###.#############
#...#.#.#.#.#.#.#...#.#r..#...#...#...#.#.#...#.#.#.#...#.........#.....#.......#
#.#.###.###.#.#.#####.#.#####.###.#.#.#.#.#.###.#.#.###############.###.#.#####.#
#.#.#...#...#.#.#.#...#.F.#...#...#.#.#.#.#...#.#.#.#...#.........#...#.#.#...#.#
#.#.#.###.#.#.#.#.#.#.###.#.###.###.#.###.###.#.#.###.#.#.#######.###.#.#.#.###.#
#.#.#...#.#.#.#...#.#...#...#.#cJ...#...#.....#.#.....#...#.#...#.#...#.#.#...#.#
#.#.###.#.#.#.#####.###.#####.#########.#######.###########.#.#.#.#####.#.###.#.#
#.#...#.#.#.#.......#.#...#.....#..p..#.#.....#...#.....#.....#.#.....#.#...#.#.#
#####.#.#.###########.#.###.#.###.#.###.#.###.#.#.#.###.#.#####.#####.#.###.#K#.#
#.....#.#...#.......U.#.....#.#...#.....#.#.#...#...#.#...#...#.#.S...#.......#.#
#.#.###.###.#.###.###.#######.#.#########.#.#########.#####.#.#.#.#######.#####.#
#.#.#...#...#.#.#.#.#.....#y..#...#.....#...#.........#.....#...#.......#.#...#w#
#.###.###.###.#.#.#.#####.#.#####.#.#.#####.#.###.#####.#####.#########.#.#.#.#.#
#...#...#.....#.#.#.......#.......#.#...#.#.#...#.#.....#.....#.......#.#n#.#.#.#
#.#.###.#.#####.#.#####.###############.#.#.###.#.#.###########.###.###.###.#.#.#
#.#...#.#.......#.....#.#.............M.#.#.#...#.#...#.........#...#..h#...#.O.#
#.#.###.#############.#G###.###########.#.#.#.###.###.#.#########.###.###.#####.#
#.#...............X...#.....#......q....#.....#.....#...........#.........#.....#
#################################################################################'''
# maze 2:
# ans for the maze below: min_steps 136 shortest_path bcefkagnldhmjoip duration = 0.9374038
# maze = '''#################
# #i.G..c...e..H.p#
# ########.########
# #j.A..b...f..D.o#
# ########@########
# #k.E..a...g..B.n#
# ########.########
# #l.F..d...h..C.m#
# #################'''
# maze 3:
# ans for the maze below: min_steps 132 shortest_path bacdfeg duration = 0.002622100000000002
# maze = '''########################
# #...............b.C.D.f#
# #.######################
# #.....@.a.B.c.d.A.e.F.g#
# ########################'''
# maze 4:
# ans for the maze below: min_steps 81 shortest_path acdgfibeh duration = 0.007309300000000005
# maze = '''########################
# #@..............ac.GI.b#
# ###d#e#f################
# ###A#B#C################
# ###g#h#i################
# ########################'''
start = timeit.default_timer()
maze_lines = maze.splitlines()
height = len(maze_lines)
width = len(maze_lines[0])
space_char = '.'
wall_char = '#'
start_y = maze.index('@') // (width+1) # +1 for \n
start_x = maze.index('@') % (width+1) # +1 for \n
# print(height, width)
# print(start_y, start_x)
keys_loc = {} # {'key': [y, x], ...}
keys_list = []
for i in range(height):
  for j in range(width):
    if maze_lines[i][j].islower():
      keys_loc[maze_lines[i][j]] = [i, j]
      keys_list.append(maze_lines[i][j])

def bfs_keys(start_key, end_key):
  maze_line_spaces = [[char != '#' for char in line] for line in maze_lines]
  key_pair_steps_doors = {}
  visited = [[False for j in range(width)] for i in range(height)]
  start_key_y = keys_loc[start_key][0]
  start_key_x = keys_loc[start_key][1]
  end_key_y = keys_loc[end_key][0]
  end_key_x = keys_loc[end_key][1]
  visiting_queue = [[start_key_y, start_key_x, 0, []]] # (y, x, step, doors)
  def process_adj(y, x, step, doors):
    target = maze_lines[y][x]
    if maze_line_spaces[y][x]:
      new_doors = doors.copy()
      if target.isupper():
        new_doors.append(target)
      visiting_queue.append([y, x, step, new_doors])
  while visiting_queue:
    front = visiting_queue.pop(0)
    y = front[0]
    x = front[1]
    step = front[2]
    doors = front[3]
    if y == end_key_y and x == end_key_x:
      return {'step': step, 'doors': doors}
    maze_line_spaces[y][x] = False
    adj_spaces = []
    # top
    if y > 0:
      process_adj(y - 1, x, step + 1, doors)
    if y < height - 1:
      process_adj(y + 1, x, step + 1, doors)
    if x > 0:
      process_adj(y, x - 1, step + 1, doors)
    if x < width - 1:
      process_adj(y, x + 1, step + 1, doors)
    # print(f'queue {visiting_queue}')
  # print(f'new_keys {new_keys}')
  # return new_keys

key_pairs_steps_doors = {}
for key1 in keys_loc:
  key_pairs_steps_doors[key1] = {}
  for key2 in keys_loc:
    if key1 == key2:
      continue
    elif key_pairs_steps_doors.get(key2) and key_pairs_steps_doors[key2].get(key1):
      key_pairs_steps_doors[key1][key2] = key_pairs_steps_doors[key2][key1]
      continue
    else:
      key_pairs_steps_doors[key1][key2] = bfs_keys(key1, key2)
# print(len(keys_loc))
# print(key_pairs_steps_doors)
# use (y, x) coordinates


def bfs(y, x, existing_keys):
  maze_line_spaces = [[char.islower() or char == space_char or char.lower() in existing_keys or char == '@' for char in line] for line in maze_lines]
  new_keys = {}
  visited = [[False for j in range(width)] for i in range(height)]
  visiting_queue = [[y, x, 0]] # (y, x, step)
  def process_adj(y, x, step):
    target = maze_lines[y][x]
    if maze_line_spaces[y][x]:
      # if target.islower():
        # print(f'{target} in {existing_keys} = {target in existing_keys}')
      if target.islower() and target not in existing_keys:
        new_keys[target] = step
      visiting_queue.append([y, x, step])
  while visiting_queue:
    front = visiting_queue.pop(0)
    y = front[0]
    x = front[1]
    maze_line_spaces[y][x] = False
    step = front[2]
    adj_spaces = []
    # top
    if y > 0:
      # target = maze_lines[y-1][x]
      # if target.islower() or target == space_char:
      #   if target.islower():
      #     keys.append(target)
      #   visiting_queue.append([y-1, x])
      process_adj(y - 1, x, step + 1)
    if y < height - 1:
      process_adj(y + 1, x, step + 1)
    if x > 0:
      process_adj(y, x - 1, step + 1)
    if x < width - 1:
      process_adj(y, x + 1, step + 1)
    # print(f'queue {visiting_queue}')
  # print(f'new_keys {new_keys}')
  return new_keys
min_steps = 10000
dp = {}
def search(key, existing_keys):
  global min_steps, dp
  # print(f'search({key},{existing_keys})')
  steps_so_far = sum(existing_keys.values())
  if len(existing_keys) == len(keys_loc):
    # print(f'min_steps {min_steps}\nkeys {existing_keys}\nsteps sum {steps_so_far}')
    if steps_so_far < min_steps:
      min_steps = steps_so_far
    return steps_so_far
  if steps_so_far > min_steps: # if steps to reach this point is alr > min steps found, skip subsequent children
    return 10000
  remaining_keys = ''.join(sorted(list(set([*keys_loc.keys()]) - set([*existing_keys])) + [key]))
  if remaining_keys in dp:
    return dp[remaining_keys]
  new_keys = {}
  if existing_keys:
    for target_key, steps_doors in key_pairs_steps_doors[key].items():
      if target_key in existing_keys:
        continue
      elif all(door.lower() in existing_keys for door in steps_doors['doors']):
        new_keys[target_key] = steps_doors['step']
  else:
    new_keys = bfs(start_y, start_x, {})
  children_steps = []
  for new_key, step in new_keys.items():
    # key_y = keys_loc[new_key][0]
    # key_x = keys_loc[new_key][1]
    # print(key_y)
    # print(key_x)
    # print(step)
    existing_keys_copy = existing_keys.copy()
    existing_keys_copy[new_key] = step
    min_steps_sum = search(new_key, existing_keys_copy)
    children_steps.append({'key': new_key, 'min_steps_sum': min_steps_sum})
  # print(f'len {len(existing_keys)} children of {existing_keys} min steps {min(children_steps)}')
  # if len(existing_keys) < 15:
  #   print(f'< 15: {existing_keys} min_steps {min_steps}')
  min_children_steps = min(children_steps, key=lambda k: k['min_steps_sum'])['min_steps_sum']
  dp[remaining_keys] = min_children_steps
  print(f'remaining_keys {remaining_keys} steps {min_children_steps}')
  print(f'{existing_keys}\n  {children_steps}\n  {min(children_steps, key=lambda k: k["min_steps_sum"])}')
  return min_children_steps

# print(f'ANS = {search("@", {})}')

# first_keys = bfs(start_y, start_x, {})
shortest_path = ''
def tsp_dp(key, remaining_keys, sum_steps, path): # sum_steps is steps until key
  global min_steps, dp, shortest_path
  # print(f'search({key},{existing_keys})')
  if not remaining_keys:
    return sum_steps
  # if sum_steps > min_steps: # if steps to reach this point is alr > min steps found, skip subsequent children
  #   return 10000
  remaining_keys_str = ''.join(sorted(remaining_keys))
  remaining_keys_and_key_str = ''.join(sorted(remaining_keys + [key]))
  # print(f'remaining_keys_and_key_str {remaining_keys_and_key_str} dp {dp}')
  if key in dp and remaining_keys_str in dp[key]:
    # print(f'{remaining_keys_str} in dp[{key}] = {dp[key][remaining_keys_str]}')
    min_children = dp[key][remaining_keys_str]
    # remaining_keys_and_key_str = ''.join(sorted(remaining_keys + [key]))
    # dp[remaining_keys_and_key_str] = key_pairs_steps_doors[key][min_children['key']]['step'] + min_children['min_steps_sum']
    return sum_steps + min_children['min_steps_sum']
  children_keys = {}
  if remaining_keys == keys_list:
    children_keys = bfs(start_y, start_x, {})
  else:
    for target_key, steps_doors in key_pairs_steps_doors[key].items():
      if target_key in remaining_keys and all(door.lower() not in remaining_keys for door in steps_doors['doors']):
        children_keys[target_key] = steps_doors['step']
  children_steps = []
  # print(f'children keys {children_keys}')
  for child_key, step in children_keys.items():
    # print(f'child key {child_key}')
    # if sum_steps + step > min_steps:
    #   print(f'sum_steps {sum_steps} + step {step} > min_step {min_steps}')
    #   print(f'child_key {child_key} rem keys {remaining_keys_str}')
    #   continue
    remaining_keys_copy = remaining_keys.copy()
    remaining_keys_copy.remove(child_key)
    remaining_keys_copy_str = ''.join(sorted(remaining_keys_copy))
    # if remaining_keys_copy_str in dp:
    #   print(f'{remaining_keys_copy_str} in dp = {dp[remaining_keys_copy_str]}')
    #   min_children = dp[remaining_keys_copy_str]
    #   min_children_sum = sum_steps + step + dp[remaining_keys_copy_str]
    # else:
    min_children_sum = tsp_dp(child_key, remaining_keys_copy, sum_steps + step, path + child_key)
    children_steps.append({'key': child_key, 'min_steps_sum': min_children_sum - sum_steps})
  # print(f'len {len(existing_keys)} children of {existing_keys} min steps {min(children_steps)}')
  min_children = min(children_steps, key=lambda k: k['min_steps_sum']) # {'key': 'a', 'min_children_sum': 1}
  # if len(remaining_keys) > 8:
  #   print(f'> 8: {remaining_keys} min_children {min_children["min_steps_sum"]}')
  dp.setdefault(key, {})[remaining_keys_str] = min_children
  # print(f'dp[{key}][{remaining_keys_str}] = {min_children}')
  # dp[''.join(sorted([key] + remaining_keys))] = min_children
  # print(f'remaining_keys {remaining_keys} steps {min_children["min_steps_sum"]}')
  # print(f'dp {dp}')
  # print(f'{remaining_keys}\n  {children_steps}\n  {min(children_steps, key=lambda k: k["min_steps_sum"])}')
  # print(f'min_steps {min_steps}\nkeys {existing_keys}\nsteps sum {steps_so_far}')
  if sum_steps + min_children["min_steps_sum"] < min_steps:
    min_steps = sum_steps + min_children["min_steps_sum"]
    k = key
    r_k = remaining_keys
    p = ''
    while len(r_k) > 0:
      r_k_s = ''.join(sorted(r_k))
      k = dp[k][r_k_s]['key']
      r_k.remove(k)
      p += k
    shortest_path = path + p
    # print(f'new shortest path {path} steps {min_steps}')
  return sum_steps + min_children["min_steps_sum"]

print(f'ANS {tsp_dp("", keys_list, 0, "")}')
stop = timeit.default_timer()
print(f'min_steps {min_steps} shortest_path {shortest_path} duration = {stop - start}')
# ANS 4620
# min_steps 4620 shortest_path lditugmxvaopyqbsefjwnhrckz duration = 6.5812673
# note that shortest path may not be exactly accurate by skipping over keys that are traversed and coming back to it but general path should be correct (see the maze 2 ans at line 83)