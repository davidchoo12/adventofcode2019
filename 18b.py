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
#.....#.....#.....#.....#.........#....@#@............#.............#...#.....#.#
#################################################################################
#...#d..#.....#.....#.......#.....#.#..@#@............#.............A.#.........#
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
# min_steps 6 shortest_path bcd duration = 0.0005542000000000047
# maze = '''#######
# #@.#Cd#
# ##.#@##
# #######
# ##@#@##
# #cB#.b#
# #######'''
# maze 3:
# min_steps 24 shortest_path abcd duration = 0.0009158000000000013
# maze = '''###############
# #d.ABC.#.....a#
# ######@#@######
# ###############
# ######@#@######
# #b.....#.....c#
# ###############'''
# maze 4:
# min_steps 32 shortest_path abcdefghijkl duration = 0.0015688000000000021
# maze = '''#############
# #DcBa.#.GhKl#
# #.###@#@#I###
# #e#d#####j#k#
# ###C#@#@###J#
# #fEbA.#.FgHi#
# #############'''
# maze 5:
# min_steps 72 shortest_path eabhcdfgikjlnmo duration = 0.010936500000000002
# maze = '''#############
# #g#f.D#..h#l#
# #F###e#E###.#
# #dCba@#@BcIJ#
# #############
# #nK.L@#@G...#
# #M###N#H###.#
# #o#m..#i#jk.#
# #############'''
# maze 6:
# min_steps 94 shortest_path bfdoelajcgnhmipk duration = 4.800232899999999
# maze = '''###################
# #i.G..c..#..e..H.p#
# ########.#.########
# #j.A..b.@#@.f..D.o#
# ###################
# #k.E..a.@#@.g..B.n#
# ########.#.########
# #l.F..d..#..h..C.m#
# ###################'''
start = timeit.default_timer()
maze_lines = maze.splitlines()
height = len(maze_lines)
width = len(maze_lines[0])
space_char = '.'
wall_char = '#'
# use (y, x) coordinates
top_left_robot_index = maze.index('@')
top_right_robot_index = maze.index('@', top_left_robot_index + 1)
bottom_left_robot_index = maze.index('@', top_right_robot_index + 1)
bottom_right_robot_index = maze.index('@', bottom_left_robot_index + 1)
robots_loc = {str(i): [index // (width+1), index % (width+1)] for i, index in enumerate([top_left_robot_index, top_right_robot_index, bottom_left_robot_index, bottom_right_robot_index])} # width+1 for \n
# print(robots_loc) # {'0': [y, x], ...}
# treat robots as keys
keys_loc = robots_loc.copy() # {'0', [y, x], ..., 'key': [y, x], ...}
keys_list = []
for i in range(height):
  for j in range(width):
    if maze_lines[i][j].islower():
      keys_loc[maze_lines[i][j]] = [i, j]
      keys_list.append(maze_lines[i][j])

def bfs(start_key):
  adj_list = {}
  maze_line_spaces = [[char != '#' for char in line] for line in maze_lines]
  key_pair_steps_doors = {}
  visited = [[False for j in range(width)] for i in range(height)]
  # if is_key:
  start_key_y = keys_loc[start_key][0]
  start_key_x = keys_loc[start_key][1]
  # else: # is robot
  #   start_key_y = robots_loc[start_key][0]
  #   start_key_x = robots_loc[start_key][1]
  visiting_queue = [[start_key_y, start_key_x, 0, []]] # (y, x, step, doors)
  def process_adj(y, x, step, doors):
    target = maze_lines[y][x]
    if maze_line_spaces[y][x]:
      new_doors = doors.copy()
      if target.islower():
        adj_list[target] = {'step': step, 'doors': new_doors}
      elif target.isupper():
        new_doors.append(target)
      visiting_queue.append([y, x, step, new_doors])
  while visiting_queue:
    front = visiting_queue.pop(0)
    y = front[0]
    x = front[1]
    step = front[2]
    doors = front[3]
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
  return adj_list

key_pairs_steps_doors = {}
for key1 in keys_loc:
  key_pairs_steps_doors[key1] = bfs(key1)
# print(key_pairs_steps_doors)

# robots_keys_steps_doors = {}
# for robot in robots_loc:
#   robots_keys_steps_doors[robot] = bfs(robot, False)
# print(robots_keys_steps_doors)

min_steps = 10000
dp = {}
shortest_path = ''
# keys = []
def tsp_dp(keys, remaining_keys, sum_steps, path): # sum_steps is steps until key
  # print(f'{keys} {remaining_keys}, {sum_steps} {path}')
  global min_steps, dp, shortest_path
  if not remaining_keys:
    return sum_steps
  if sum_steps > min_steps: # if steps to reach this point is alr > min steps found, skip subsequent children
    # print(f'sum steps > min steps ({min_steps})')
    return 10000
  keys_str = ''.join(keys) # doesn't need to be sorted cos keys in each position is mutually exclusive based on its zone
  remaining_keys_str = ''.join(sorted(remaining_keys))
  # remaining_keys_and_key_str = ''.join(sorted(remaining_keys + [key]))
  # print(f'remaining_keys_and_key_str {remaining_keys_and_key_str} dp {dp}')
  if keys_str in dp and remaining_keys_str in dp[keys_str]:
    # print(f'{remaining_keys_str} in dp[{keys_str}] = {dp[keys_str][remaining_keys_str]}')
    min_children = dp[keys_str][remaining_keys_str]
    return sum_steps + min_children['min_steps_sum']
  keys_children_keys = {}
  # if remaining_keys == keys_list:
  #   keys_children_keys = robots_keys_steps_doors
  # else:
  for key in keys:
    keys_children_keys[key] = {}
    for target_key, steps_doors in key_pairs_steps_doors[key].items():
      if target_key in remaining_keys and all(door.lower() not in remaining_keys for door in steps_doors['doors']):
        keys_children_keys[key][target_key] = steps_doors['step']
  # print(f'keys children keys {keys_children_keys}')
  children_steps = []
  for i, children_keys in enumerate(keys_children_keys.values()):
    for child_key, step in children_keys.items():
      # print(f'child key {child_key}')
      # if sum_steps + step > min_steps:
      #   print(f'sum_steps {sum_steps} + step {step} > min_step {min_steps}')
      #   print(f'child_key {child_key} rem keys {remaining_keys_str}')
      #   continue
      keys_copy = keys.copy()
      keys_copy[i] = child_key
      keys_copy_str = ''.join(keys_copy)
      remaining_keys_copy = remaining_keys.copy()
      remaining_keys_copy.remove(child_key)
      remaining_keys_copy_str = ''.join(sorted(remaining_keys_copy))
      # if remaining_keys_copy_str in dp:
      #   print(f'{remaining_keys_copy_str} in dp = {dp[remaining_keys_copy_str]}')
      #   min_children = dp[remaining_keys_copy_str]
      #   min_children_sum = sum_steps + step + dp[remaining_keys_copy_str]
      # else:
      min_children_sum = tsp_dp(keys_copy, remaining_keys_copy, sum_steps + step, path + child_key)
      children_steps.append({'next_key': child_key, 'next_keys': keys_copy_str, 'min_steps_sum': min_children_sum - sum_steps})
  # print(f'len {len(existing_keys)} children of {existing_keys} min steps {min(children_steps)}')
  min_children = min(children_steps, key=lambda k: k['min_steps_sum']) # {'key': 'a', 'min_children_sum': 1}
  # if len(path) < 15:
  #   print(f'< 15: {path} min_children {min_children["min_steps_sum"]}')
  dp.setdefault(keys_str, {})[remaining_keys_str] = min_children
  # print(f'dp[{keys_str}][{remaining_keys_str}] = {min_children}')
  # dp[''.join(sorted([key] + remaining_keys))] = min_children
  # print(f'remaining_keys {remaining_keys} steps {min_children["min_steps_sum"]}')
  # print(f'dp {dp}')
  # print(f'{remaining_keys}\n  {children_steps}\n  {min(children_steps, key=lambda k: k["min_steps_sum"])}')
  # print(f'min_steps {min_steps}\nkeys {existing_keys}\nsteps sum {steps_so_far}')
  if sum_steps + min_children["min_steps_sum"] < min_steps:
    min_steps = sum_steps + min_children["min_steps_sum"]
    k = keys
    r_k = remaining_keys
    p = ''
    k_s = ''.join(keys)
    while len(r_k) > 0:
      r_k_s = ''.join(sorted(r_k))
      # print(f'{k_s} {r_k_s}')
      # if k_s not in dp:
      #   print(f'k_s {k_s}')
      # elif r_k_s not in dp[k_s]:
      #   print(f'r_k_s {r_k_s}')
      #   print(f'dp[{k_s}] {dp[k_s]}')
      curr_dp = dp[k_s][r_k_s]
      # print(f'dp[{k_s}][{r_k_s}] {dp[k_s][r_k_s]}')
      # print(f'curr_dp {curr_dp}')
      k_s = curr_dp['next_keys']
      k = curr_dp['next_key']
      r_k.remove(k)
      p += k
    shortest_path = path + p
    # print(f'new shortest path {path} steps {min_steps}')
  return sum_steps + min_children["min_steps_sum"]

print(f'ANS {tsp_dp([*robots_loc.keys()], keys_list, 0, "")}')
stop = timeit.default_timer()
print(f'min_steps {min_steps} shortest_path {shortest_path} duration = {stop - start}')
# ANS 1564
# min_steps 1564 shortest_path bsaltidvxugmohwknqypjefcrz duration = 20.0285911