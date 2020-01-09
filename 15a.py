import random

code = '''3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,102,1,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1106,0,124,102,1,1034,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,1001,1035,0,1040,1002,1038,1,1043,101,0,1037,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,102,1,1035,1040,101,0,1038,1043,1001,1037,0,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,7,1032,1006,1032,165,1008,1040,37,1032,1006,1032,165,1102,1,2,1044,1106,0,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,39,1044,1105,1,224,1101,0,0,1044,1105,1,224,1006,1044,247,102,1,1039,1034,102,1,1040,1035,101,0,1041,1036,102,1,1043,1038,102,1,1042,1037,4,1044,1106,0,0,35,37,2,26,91,30,85,34,87,18,47,29,50,23,7,46,94,2,26,42,36,23,3,32,65,21,63,18,54,31,52,75,4,35,24,24,74,33,81,89,75,50,36,43,7,20,45,9,23,10,70,12,81,62,12,51,3,5,96,7,93,90,12,41,5,52,30,91,12,62,34,44,92,68,9,81,9,6,30,38,63,27,51,3,44,47,27,86,41,1,73,78,15,34,98,9,63,66,21,89,96,5,9,36,21,97,6,26,75,14,86,16,82,21,23,91,25,15,66,33,2,50,26,18,61,73,17,49,15,99,19,68,96,33,23,12,81,11,51,19,30,56,74,27,40,76,15,49,11,24,50,27,50,36,77,36,16,22,80,86,11,85,20,87,24,26,6,64,35,27,65,32,86,42,99,30,78,68,24,67,82,4,76,63,36,4,46,21,72,68,17,21,69,71,36,82,22,57,1,29,95,59,18,48,40,91,7,44,22,64,5,52,20,20,86,34,9,67,74,22,13,31,97,23,19,78,19,12,80,19,82,83,11,26,5,10,74,2,42,5,94,26,79,51,33,15,47,9,12,84,20,37,85,63,27,92,16,10,82,64,15,50,75,12,68,51,37,87,10,51,18,11,13,99,97,30,33,48,2,45,29,22,45,20,49,14,78,33,41,89,4,67,21,40,42,20,4,34,64,98,32,77,28,79,9,51,91,58,19,45,56,4,10,3,52,47,65,11,21,53,25,57,78,33,16,70,88,34,56,37,86,30,4,84,91,86,90,37,37,25,59,2,96,25,19,69,6,11,67,83,38,8,49,18,17,21,56,20,43,89,8,78,30,80,52,29,9,65,1,1,65,27,84,23,8,33,99,71,28,38,45,14,40,31,45,44,12,94,12,65,23,96,5,93,50,35,84,10,34,81,2,51,15,11,92,69,20,65,27,68,86,76,36,49,38,79,92,38,72,8,32,80,29,41,7,15,78,38,5,10,61,24,44,38,19,80,9,60,95,95,33,48,13,51,32,57,84,97,1,51,36,6,51,96,16,62,32,13,93,4,79,40,2,68,74,38,4,30,82,17,67,51,68,29,3,85,13,5,2,30,71,36,77,35,78,23,87,22,7,78,5,60,2,11,42,15,68,89,66,93,31,38,31,81,8,65,22,7,27,83,59,21,12,73,64,72,40,38,59,20,29,92,20,7,65,16,86,81,12,44,77,97,30,19,49,61,24,29,24,31,87,89,31,42,80,17,91,23,18,91,10,53,5,17,53,30,96,96,34,83,34,18,68,79,97,18,4,56,37,33,62,31,79,99,32,14,99,87,83,53,34,26,17,70,59,31,12,42,91,32,93,5,54,8,10,83,20,58,92,30,71,24,34,60,3,9,64,72,12,70,14,22,69,38,27,77,31,84,8,54,44,58,9,30,95,22,12,61,95,21,81,71,5,64,44,7,71,4,17,41,2,89,16,20,93,88,20,31,45,28,49,91,15,72,43,6,21,82,15,25,99,8,11,34,18,93,50,15,15,98,27,34,44,38,15,29,79,42,14,86,68,56,7,3,97,21,58,11,33,67,6,53,23,71,16,58,74,17,92,17,14,98,23,35,60,32,70,54,1,82,2,41,32,68,91,27,80,6,25,55,93,23,52,91,3,95,44,3,42,70,23,16,54,36,36,59,5,63,27,40,11,73,34,48,29,73,36,74,77,58,25,55,25,45,7,58,53,49,8,95,13,84,23,58,37,42,6,70,36,58,73,55,14,51,5,99,95,61,20,65,0,0,21,21,1,10,1,0,0,0,0,0,0'''

wall_coords = []
travelled_coords = []
curr_coord = [0,0]
next_coord = [0,1]
next_input = 1
# 1 = north, 2 = south, 3 = west, 4 = east
direction_seq = [1,3,1,4,1,2,1,2,4,2,3,1,3,2,3,4,3]
curr_dir_i = 0
curr_dir = 1
right_of = [0, 4, 3, 1, 2]
left_of = [0, 3, 4, 2, 1]
opp_of = [0, 2, 1, 4, 3]
curr_dir_hit = -1
next_dir_hit = -1
next2_dir_hit = -1

def runcode(code_str, input_handler, output_handler):
  x = list(map(int, code_str.split(',')))
  x += [0] * 10 * len(x)
  i = 0
  relative_base = 0
  while i < len(x):
    op = x[i] % 100
    if op == 99:
      return
    mode1 = int(x[i] / 100 % 10)
    param1 = x[x[i+1]] if mode1 == 0 else x[i+1] if mode1 == 1 else x[relative_base + x[i+1]]
    if op == 3:
      input_val = input_handler()
      if mode1 == 2:
        x[relative_base + x[i+1]] = input_val
      else:
        x[x[i+1]] = input_val
      i += 2
    elif op == 4:
      output_handler(param1)
      i += 2
    elif op == 9:
      relative_base += param1
      i += 2
    else:
      mode2 = int(x[i] / 1000 % 10)
      param2 = x[x[i+2]] if mode2 == 0 else x[i+2] if mode2 == 1 else x[relative_base + x[i+2]]
      if op == 5:
        if param1:
          i = param2
        else:
          i += 3
      elif op == 6:
        if not param1:
          i = param2
        else:
          i += 3
      else:
        mode3 = int(x[i] / 10000 % 10)
        param3 = x[x[i+3]] if mode3 == 0 else x[i+3] if mode3 == 1 else x[relative_base + x[i+3]]
        if op == 1:
          if mode3 == 2:
            x[relative_base + x[i+3]] = param1 + param2
          else:
            x[x[i+3]] = param1 + param2
          i += 4
        elif op == 2:
          if mode3 == 2:
            x[relative_base + x[i+3]] = param1 * param2
          else:
            x[x[i+3]] = param1 * param2
          i += 4
        elif op == 7:
          if mode3 == 2:
            x[relative_base + x[i+3]] = 1 if param1 < param2 else 0
          else:
            x[x[i+3]] = 1 if param1 < param2 else 0
          i += 4
        elif op == 8:
          if mode3 == 2:
            x[relative_base + x[i+3]] = 1 if param1 == param2 else 0
          else:
            x[x[i+3]] = 1 if param1 == param2 else 0
          i += 4

def input_handler():
  global next_coord
  # input_char = input()
  # next_input = 1 if input_char == 'w' else 2 if input_char == 's' else 3 if input_char == 'a' else 4
  curr_x = curr_coord[0]
  curr_y = curr_coord[1]
  if next_input == 1:
    next_coord = [curr_x, curr_y + 1]
  elif next_input == 2:
    next_coord = [curr_x, curr_y - 1]
  elif next_input == 3:
    next_coord = [curr_x - 1, curr_y]
  elif next_input == 4:
    next_coord = [curr_x + 1, curr_y]
  print(f'input {next_input}')
  return next_input

def output_handler(output):
  global curr_coord, curr_dir_i, next_input, curr_dir, curr_dir_hit, next_dir_hit, next2_dir_hit
  if output == 0: # has wall
    if next_coord not in wall_coords:
      wall_coords.append(next_coord)
  else: # free or found
    if curr_coord not in travelled_coords:
      travelled_coords.append(curr_coord)
    curr_coord = next_coord
  if output == 2: # found
    curr_coord = next_coord
    print(f'FOUND at {curr_coord}!')
    print_maze()
    exit(0)
  print_maze()
  # logic (example curr direction is north)
  # north
  #   wall - east
  #     wall - west
  #       wall - go to "south"
  #       free - go to "west"
  #     free - go to "east"
  #   free - east
  #     wall - go to "north"
  #     free - go to "east"
  if curr_dir_hit == -1: # handle for moving in curr dir
    curr_dir_hit = output
    next_input = right_of[curr_dir]
    next_dir_hit = -1 # next handle next dir
    return
  elif next_dir_hit == -1: # handle for moving in next dir
    next_dir_hit = output
    if next_dir_hit == 1: # curr dir wall/free, next dir free
      curr_dir = right_of[curr_dir]
      next_input = right_of[curr_dir]
      curr_dir_hit = 1 # curr dir is now free
      next_dir_hit = -1 # next handle next dir
    elif curr_dir_hit == 0: # curr dir wall, next dir wall
      next_input = left_of[curr_dir]
      next2_dir_hit = -1 # next handle next2 dir
    elif curr_dir_hit == 1: # curr dir free, next dir wall
      next_input = curr_dir
      curr_dir_hit = -1 # next handle curr dir
    return
  elif next2_dir_hit == -1: # handle for moving in next 2 dir
    next2_dir_hit = output
    if next2_dir_hit == 0: # curr dir wall, next dir wall, next2 dir wall
      curr_dir = opp_of[curr_dir]
      next_input = right_of[curr_dir]
      curr_dir_hit = 1 # curr dir is now free
      next_dir_hit = -1 # next handle next dir
    elif next2_dir_hit == 1: # curr dir wall, next dir wall, next2 dir free
      curr_dir = left_of[curr_dir]
      next_input = right_of[curr_dir]
      curr_dir_hit = 1 # curr dir is now free
      next_dir_hit = -1 # next handle next dir
    return

  # curr_x = curr_coord[0]
  # curr_y = curr_coord[1]
  # north_coord = [curr_x, curr_y + 1]
  # south_coord = [curr_x, curr_y - 1]
  # west_coord = [curr_x - 1, curr_y]
  # east_coord = [curr_x + 1, curr_y]
  # next_input = 0
  # if north_coord not in wall_coords and north_coord not in travelled_coords:
  #   next_input = 1
  # elif east_coord not in wall_coords and east_coord not in travelled_coords:
  #   next_input = 4
  # elif south_coord not in wall_coords and south_coord not in travelled_coords:
  #   next_input = 2
  # elif west_coord not in wall_coords and west_coord not in travelled_coords:
  #   next_input = 3
  # if next_input == 0:
  #   possible_next_inputs = []
  #   if north_coord not in wall_coords:
  #     possible_next_inputs.append(1)
  #   elif east_coord not in wall_coords:
  #     possible_next_inputs.append(4)
  #   elif south_coord not in wall_coords:
  #     possible_next_inputs.append(2)
  #   elif west_coord not in wall_coords:
  #     possible_next_inputs.append(3)
  #   next_input = possible_next_inputs[random.randint(0, len(possible_next_inputs) - 1)]

  # curr_dir_i = (curr_dir_i + 1) % len(direction_seq)
  # next_input = direction_seq[curr_dir_i]

def print_maze():
  coords = wall_coords + travelled_coords + [curr_coord]
  # if not coords:
  #   print('no coords')
  #   return
  x_min = min(coords, key=lambda e: e[0])[0]
  x_max = max(coords, key=lambda e: e[0])[0]
  y_min = min(coords, key=lambda e: e[1])[1]
  y_max = max(coords, key=lambda e: e[1])[1]
  # print(x_min)
  # print(x_max)
  # print(y_min)
  # print(y_max)
  # print(x_max - x_min)
  # print(y_max - y_min)
  # print(coords)

  for i in range(y_max, y_min - 1, -1):
    for j in range(x_min, x_max + 1):
      if curr_coord == [j, i]:
        print('D', end='')
      elif [j, i] in wall_coords:
        print('#', end='')
      elif [j, i] in travelled_coords:
        print('.', end='')
      else:
        print(' ', end='')
    print()
  print()

runcode(code, input_handler, output_handler)

# final output (D is the final curr_coord) (hugging right wall)
# FOUND at [-14, -16]!
             #####
            #.....#
     ########.   .#
    #.......#.   .#
   ##.     .#.   .######
  #...     .#... .......#
  #.       .###.       .#
  #. ...   .....       .#...
  #. .#.               .#.#.
  #. .#.....           . .#.
  #. .#####.             .#.
  #. .#.....             .#.....
  #. .#.                 .#####.
  #...#...   ........... .#.....
   ### ##.   .#########. .#.
  #...#...   .#.....#.#...#...
  #.###.     .#.###.#.#######.
  #...#. .....#.#...#...#.....
   ##.#. .#####.#.#####.#.
  #...#. .#.....#.#.....#.....
  #.###. .#.#####.#.###.#####.
  #...#...#.#.....#.#...#.....
   ##.#####.#####.#.#.###.
  #...#.....#...#...#...#.
  #.###.   .#. .#### ##.#.
  #..... D .#. .....#...#.
  #.     .#.#.     .#####.
  #.......#...     .......
   #######

# hugging left wall by swapping right_of and left_of (took a lot longer)
#  ############### ### ########### #######
# #...............#...#...........#.......#
# #.#.###########.###.#.#.#########.#.####
# #.#.....#...#.#.....#.#...........#.....#
#  ######.#.#.#.#####.#.#################.#
# #.......#.#...#.....#.#.....#.........#.#
# #.#######.#####.#####.###.#.#.#######.#.#
# #.#.....#.......#...#.#...#.#.....#.#.#.#
# #.#.###.#########.#.#.#.###.#####.#.#.#.#
# #...#.#.#...#.....#...#.#...#.....#...#.#
# #.###.#.#.#.#.#########.#####.#####.###.#
# #.....#...#.........#...#...#.....#.#...#
#  ####.#### ########.#.###.#.#.###.#.###.#
# #.........#.....#...#.#...#.#...#.#.#...#
# #.######## .###.#.###.#.###.#####.#.#.#.#
# #.#....... .#.#.#.....#...#.......#...#.#
#  # .#####. .#.#. ######.#.######## ####.#
#  ...#...#. ...#.......#.#.........#...#.#
#  .#####.#.   .#######. ####.#####.#.###.#
#  .#...#.#.....#.....#.#...#...#.#.#.....#
#  .#. .#.#######.###.#.#. .###.#.#.######
#  .#. .....#.#...#.#.#.#. .#.....#.#.....#
#  .#.     .#.#.###.#.###. .#####.#.#.###.#
#  .#. .....#.......#..... .....#.#...#...#
#  .#. .#################.     .#.#####.#.#
#  ... ...#.............#. .....#.#...#.#.#
#        .#.#.         .#. .#######.#.#.#.#
#      ...#.#.         ... ...#.....#...#.#
#      .#####.               .###.#.#####.#
#      .#.....           .....#...#.#...#.#
#      .#.               .#####.#####.#.##
#      .#.               .....#.......#...#
#      .#.                   .#.#########.#
#      ...               .....#.#...#.....#
#                        .#####.###.#.###.#
#      ..... ...         .#.........#.#...#
#      .###. .#.         .#.#########.#.##
#  .....#D#. .#.....     .#...#.....#.#.#.#
#  .#####.#. .#####.     .#####.###.#.#.#.#
#  .......#.......#.............#.....#...#
#          ####### ############# ##### ###

# manual trace (missed the tracing through gap marked G) (digits indicate every tenths step on shortest path)
             #####
            #.....#
     ########.###.#
    #4......#2#.#.#
   ##.#####.#.#.#.######
  #...#...#.#...#1......#
  #.#####.#.###.#######.####
  #.#6..#.#3....#.....#.#...#
  #.#.#.#.#######.###.#.#.#.#
  #.#.#.....#.#...#.#.#0#.#.#
  #.#.#####.#.#.###.#.###.#.####
  #5#.#....7#.......#....2#3....#
  #.#.#.#################.#####.#
  #...#...#..........1..#.#4....#
   ### ##.#.#.#########.#.#.####
  #...#..8#.#0#.....#.#...#...#
  #.###.#####.#.###.#.#######.#      ###
  #...#.#.....#.#...#...#5....#G    #...#
   ##.#.#.#####.#.#####.#.#### .#####.#.##
  #...#.#.#.....#.#.....#.....#.......#...#
  #.###.#.#.#####.#.###.#####.#.#########.#
  #...#..9#.#.....#.#...#..6..#.#...#.....#
   ##.#####.#####.#.#.###.#####.###.#.###
  #...#.....#...#...#...#.#.........#.#
  #.###.###.#.#.#### ##.#.#.#########.#
  #....0#D#.#.#8....#...#.#...#.....#.#
  #.#####.#.#.#####.#####.#####.###.#.#
  #....1..#9......#....7........#.....#
   ####### ####### ############# #####
# ans 214