code = '109,424,203,1,21102,11,1,0,1106,0,282,21102,18,1,0,1106,0,259,1201,1,0,221,203,1,21102,31,1,0,1106,0,282,21101,38,0,0,1106,0,259,21002,23,1,2,22102,1,1,3,21101,1,0,1,21102,57,1,0,1105,1,303,2102,1,1,222,20101,0,221,3,20101,0,221,2,21102,259,1,1,21101,80,0,0,1106,0,225,21101,0,44,2,21102,91,1,0,1105,1,303,1201,1,0,223,20101,0,222,4,21101,0,259,3,21102,225,1,2,21101,225,0,1,21102,118,1,0,1105,1,225,21002,222,1,3,21101,100,0,2,21101,133,0,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1106,0,259,2102,1,1,223,20102,1,221,4,21002,222,1,3,21102,1,12,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,108,20207,1,223,2,21002,23,1,1,21102,-1,1,3,21101,0,214,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2102,1,-4,249,21201,-3,0,1,22101,0,-2,2,22101,0,-1,3,21101,0,250,0,1105,1,225,22102,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21101,0,343,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21101,0,384,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2106,0,0'

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

x = 0
y = 0
input_x = True
def input_handler():
  global input_x
  if input_x:
    input_x = False
    # x = int(input())
    return x
  else:
    input_x = True
    # y = int(input())
    return y

def output_handler(output):
  global in_range
  in_range = output
  # print(output)

# while True:
#   runcode(code, input_handler, output_handler)

# for i in range(50):
#   # outputs.append([])
#   for j in range(50):
#     y = i
#     x = j
#     runcode(code, input_handler, output_handler)

# graph = '\n'.join([''.join([str(o) for o in outputs[i*50:i*50 + 50]]) for i in range(50)])
# print(graph)
# print(sum(outputs))

y = 1000
left = 1500
right = 1500
# left = 138
# right = 165
# left_right = [[138, 165]] # starting at 100
# while len(left_right) < 101 or left_right[y - 100][1] < left + 100 or left_right[y - 101][1] > left + 100
# right = 0
# found_left = False
# found_right = False

def fibonacci_search(is_left, start_x):
  global x, in_range
  prev2_step = 0
  prev_step = 0
  step = 1 if is_left else -1
  in_range = -1
  prev_in_range = -1
  prev_x = -1
  x = start_x
  while True:
    runcode(code, input_handler, output_handler)
    # if is_left:
    #   print(f'left {x}, prev_left {prev_x}, in_range {in_range}, prev_in_range {prev_in_range}, step {step}')
    # else:
    #   print(f'right {x}, prev_right {prev_x}, in_range {in_range}, prev_in_range {prev_in_range}, step {step}')
    if not prev_in_range and in_range and ((is_left and prev_x + 1 == x) or (not is_left and x + 1 == prev_x)):
      break
    prev_x = x
    if not in_range:
      if prev_in_range:
        prev2_step = 0
        prev_step = 0
        step = 1 if is_left else -1
      else: # prev not in range
        prev2_step = prev_step
        prev_step = step
        step = prev_step + prev2_step
      x += step
    else: # in range
      if prev_in_range:
        prev2_step = prev_step
        prev_step = step
        step = prev_step + prev2_step
      else: # prev not in range
        prev2_step = 0
        prev_step = 0
        step = 1 if is_left else -1
      x -= step
    prev_in_range = in_range
  return x

# while len(left_right) < 101 or left_right[y - 100][1] < left + 100 or left_right[y - 101][1] > left + 100
prev2_step = 0
prev_step = 0
step = 1
prev_top_y_in_range = True
prev_y = -1
y = 964
length = 100
while True:
  curr_left = fibonacci_search(True, int(y * 1.4))
  curr_right = fibonacci_search(False, int(y * 1.5))
  y -= 1
  x = curr_left
  runcode(code, input_handler, output_handler)
  while in_range:
    x -= 1
    runcode(code, input_handler, output_handler)
  above_left = x + 1
  y -= length - 2
  top_left = fibonacci_search(True, int(y * 1.4))
  top_right = fibonacci_search(False, int(y * 1.6))
  # print(f'y {y} found left {top_left} right {top_right}')
  y -= 1
  x = top_right
  runcode(code, input_handler, output_handler)
  while not in_range:
    x -= 1
    runcode(code, input_handler, output_handler)
  above_top_right = x
  y += length
  above_y_out_range = above_left + length - 1 > above_top_right
  top_y_in_range = curr_left + length - 1 <= top_right
  print(f'top y {y - length + 1} left {top_left} right {top_right}')
  print(f'bottom y {y} left {curr_left} right {curr_right}')
  print(f'above top y {y - length} right {above_top_right}')
  print(f'above bottom y {y - 1} left {above_left}')
  print(f'y {y}, prev_y {prev_y}, above_y_out_range {above_y_out_range}, top_y_in_range {top_y_in_range}, step {step}')
  if above_y_out_range and top_y_in_range:
    print(f'FOUND top left coords x {curr_left} y {y - length + 1}')
    break
  prev_y = y
  if not top_y_in_range:
    if prev_top_y_in_range:
      prev2_step = 0
      prev_step = 0
      step = 1
    else: # prev not in range
      prev2_step = prev_step
      prev_step = step
      step = prev_step + prev2_step
    y += step
  else: # in range
    if prev_top_y_in_range:
      prev2_step = prev_step
      prev_step = step
      step = prev_step + prev2_step
    else: # prev not in range
      prev2_step = 0
      prev_step = 0
      step = 1
    y -= step
  prev_top_y_in_range = top_y_in_range

# ans 13280865
# output
# top y 865 left 1192 right 1427
# bottom y 964 left 1328 right 1590
# above top y 864 right 1425
# above bottom y 963 left 1327
# y 964, prev_y -1, above_y_out_range True, top_y_in_range True, step 1
# FOUND top left coords x 1328 y 865