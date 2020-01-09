code_str = '3,8,1005,8,351,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,28,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,51,1006,0,85,2,1109,8,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,80,1,2,2,10,1,1007,19,10,1,1001,13,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,113,1,2,1,10,1,1109,17,10,1,108,20,10,2,1005,3,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,151,2,5,19,10,1,104,19,10,1,109,3,10,1006,0,78,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,189,1006,0,3,2,1004,1,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,218,1,1008,6,10,1,104,8,10,1006,0,13,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,251,1006,0,17,1006,0,34,1006,0,24,1006,0,4,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,285,1006,0,25,2,1103,11,10,1006,0,75,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,316,2,1002,6,10,1006,0,30,2,106,11,10,1006,0,21,101,1,9,9,1007,9,1072,10,1005,10,15,99,109,673,104,0,104,1,21101,0,937151009684,1,21101,0,368,0,1105,1,472,21102,386979963796,1,1,21102,379,1,0,1106,0,472,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,179410325723,0,1,21101,426,0,0,1106,0,472,21101,0,179355823195,1,21102,437,1,0,1106,0,472,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,825460785920,1,21101,460,0,0,1105,1,472,21102,1,838429614848,1,21102,1,471,0,1105,1,472,99,109,2,21202,-1,1,1,21102,40,1,2,21102,1,503,3,21101,493,0,0,1105,1,536,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,498,499,514,4,0,1001,498,1,498,108,4,498,10,1006,10,530,1101,0,0,498,109,-2,2106,0,0,0,109,4,2101,0,-1,535,1207,-3,0,10,1006,10,553,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21101,0,1,3,21101,572,0,0,1105,1,577,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,600,2207,-4,-2,10,1006,10,600,21202,-4,1,-4,1106,0,668,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21102,619,1,0,1105,1,577,22102,1,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,638,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,660,22101,0,-1,1,21101,660,0,0,106,0,535,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0'

travelled_coords = []
white_coords = [[0,0]]

def step(curr, compass):
  # 0 = up, 1 = right, 2 = down, 3 = left
  x = curr[0]
  y = curr[1]
  if compass == 0:
    curr = [x, y + 1]
  elif compass == 1:
    curr = [x + 1, y]
  elif compass == 2:
    curr = [x, y - 1]
  elif compass == 3:
    curr = [x - 1, y]
  return curr

def runcode(code_str, inputs=[]):
  # print(f'runcode called with inputs: {inputs}')
  x = list(map(int, code_str.split(',')))
  x += [0] * 10 * len(x)
  inputsi = 0
  i = 0
  returnvalue = 0
  paint = -1
  turn = -1
  relative_base = 0
  curr = [0, 0]
  compass = 0 # 0 = up, 1 = right, 2 = down, 3 = left
  while i < len(x):
    op = x[i] % 100
    if op == 99:
      # print('exiting runcode')
      return [0, returnvalue]
    mode1 = int(x[i] / 100 % 10)
    param1 = x[x[i+1]] if mode1 == 0 else x[i+1] if mode1 == 1 else x[relative_base + x[i+1]]
    if op == 3:
      # print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      input_int = 1 if white_coords.count(curr) > 0 else 0
      # print(f'curr {curr}')
      # print(f'input {input_int}')
      if mode1 == 2:
        x[relative_base + x[i+1]] = input_int
      else:
        x[x[i+1]] = input_int
      i += 2
    elif op == 4:
      # print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      # print(f'output {param1}')
      if paint == -1: # if first output
        paint = param1
        turn = -1 # reset second output
        # print(f'{curr} = {paint}')
        if paint == 1 and not white_coords.count(curr):
          white_coords.append(curr)
        if paint == 0 and white_coords.count(curr):
          white_coords.remove(curr)
        travelled_coords.append(curr)
      elif turn == -1: # if second output
        turn = param1
        paint = -1 # reset first output
        if turn == 0: # turn left
          compass -= 1
        elif turn == 1: # turn right
          compass += 1
        compass %= 4
        curr = step(curr, compass)
      else:
        print(f'unexpected output {param1}')
      i += 2
    elif op == 9:
      # print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      relative_base += param1
      # print(f'relative_base {relative_base}')
      i += 2
    else:
      mode2 = int(x[i] / 1000 % 10)
      param2 = x[x[i+2]] if mode2 == 0 else x[i+2] if mode2 == 1 else x[relative_base + x[i+2]]
      if op == 5:
        # print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}', end = ' |')
        if param1:
          i = param2
        else:
          i += 3
      elif op == 6:
        # print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}', end = ' |')
        if not param1:
          i = param2
        else:
          i += 3
      else:
        mode3 = int(x[i] / 10000 % 10)
        param3 = x[x[i+3]] if mode3 == 0 else x[i+3] if mode3 == 1 else x[relative_base + x[i+3]]
        if op == 1:
          # print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}', end = ' |')
          if mode3 == 2:
            x[relative_base + x[i+3]] = param1 + param2
          else:
            x[x[i+3]] = param1 + param2
          i += 4
        elif op == 2:
          # print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}', end = ' |')
          if mode3 == 2:
            x[relative_base + x[i+3]] = param1 * param2
          else:
            x[x[i+3]] = param1 * param2
          i += 4
        elif op == 7:
          # print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}', end = ' |')
          if mode3 == 2:
            x[relative_base + x[i+3]] = 1 if param1 < param2 else 0
          else:
            x[x[i+3]] = 1 if param1 < param2 else 0
          i += 4
        elif op == 8:
          # print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}', end = ' |')
          if mode3 == 2:
            x[relative_base + x[i+3]] = 1 if param1 == param2 else 0
          else:
            x[x[i+3]] = 1 if param1 == param2 else 0
          i += 4

runcode(code_str)

print('after runcode')
# print(travelled_coords)
# print(white_coords)
# unique_travelled_coords = set([f'{x} {y}' for [x, y] in travelled_coords])
# print(len(unique_travelled_coords))
# print(len(travelled_coords))

# white_coords = sorted(white_coords, key=lambda e: e[0])
# white_coords = sorted(white_coords, key=lambda e: e[1], reverse=True)
x_min = min(white_coords, key=lambda e: e[0])[0]
x_max = max(white_coords, key=lambda e: e[0])[0]
y_min = min(white_coords, key=lambda e: e[1])[1]
y_max = max(white_coords, key=lambda e: e[1])[1]
print(x_min)
print(x_max)
print(y_min)
print(y_max)
print(white_coords)

for i in range(y_max, y_min - 1, -1):
  for j in range(x_min, x_max + 1):
    if white_coords.count([j, i]):
      print('0', end='')
    else:
      print(' ', end='')
  print()
# output:
# 000  0  0 0000 000   00  0000 000  000
# 0  0 0 0  0    0  0 0  0    0 0  0 0  0
# 0  0 00   000  0  0 0  0   0  0  0 0  0
# 000  0 0  0    000  0000  0   000  000
# 0    0 0  0    0    0  0 0    0 0  0
# 0    0  0 0    0    0  0 0000 0  0 0