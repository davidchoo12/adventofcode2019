code_str = '3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99'
code = list(map(int, code_str.split(',')))

def runcode(x, inputs=[]):
  print(f'runcode called with inputs: {inputs}')
  inputsi = 0
  i = 0
  returnvalue = 0
  while i < len(x):
    op = x[i] % 100
    if op == 99:
      print('exiting runcode')
      return [0, returnvalue]
    mode1 = int(x[i] / 100 % 10)
    param1 = x[i+1] if mode1 else x[x[i+1]]
    if op == 3:
      print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      if inputsi >= len(inputs):
        print('exiting runcode (inputs cleared)')
        return [1, returnvalue]
      x[x[i+1]] = inputs[inputsi]
      # x[x[i+1]] = int(input())
      print(f'input {inputs[inputsi]}', end = ' |')
      inputsi += 1
      i += 2
    elif op == 4:
      print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      # print(x[x[i+1]])
      returnvalue = x[x[i+1]]
      i += 2
    else:
      mode2 = int(x[i] / 1000 % 10)
      param2 = x[i+2] if mode2 else x[x[i+2]]
      if op == 5:
        print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}', end = ' |')
        if param1:
          i = param2
        else:
          i += 3
      elif op == 6:
        print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}', end = ' |')
        if not param1:
          i = param2
        else:
          i += 3
      else:
        mode3 = int(x[i] / 10000 % 10)
        param3 = x[i+3] if mode3 else x[x[i+3]]
        if op == 1:
          print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}', end = ' |')
          x[x[i+3]] = param1 + param2
          i += 4
        elif op == 2:
          print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}', end = ' |')
          x[x[i+3]] = param1 * param2
          i += 4
        elif op == 7:
          print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}', end = ' |')
          x[x[i+3]] = 1 if param1 < param2 else 0
          i += 4
        elif op == 8:
          print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}', end = ' |')
          x[x[i+3]] = 1 if param1 == param2 else 0
          i += 4

# src: https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
def permutations(lst):
  if len(lst) == 0:
    return []
  if len(lst) == 1:
    return [lst]
  l = []
  for i in range(len(lst)):
    m = lst[i]
    remLst = lst[:i] + lst[i+1:]
    for p in permutations(remLst):
      l.append([m] + p)
  return l

result_max = 0
permutation_max = []

for permutation in permutations(list(range(9, 4, -1))):
  # outpipe = [0]
  input_queues = list(map(lambda e: [e], permutation))
  input_queues[0].append(0)
  halted = list(map(lambda e: False, permutation))
  print(permutation)
  # print(input_queues)
  # print(halted)
  while not all(halted):
    for i in range(len(input_queues)):
      result = runcode(list(map(int, code_str.split(','))), input_queues[i])
      if result[0] == 0: # exited successfully
        print('exited successfully')
        # print(input_queues[i])
        # print(result)
        halted[i] = True
      input_queues[(i + 1) % len(input_queues)].append(result[1])
      # print(i)
      # print(input_queues)
  print(result)

  # for phase in permutation:
  #   print(f'inputting: {[phase] + outpipe}')
  #   outpipe = runcode(x, [phase] + outpipe)
  # print(f'permutation: {permutation}, input_queues: {input_queues}')
  if result[-1] > result_max:
    result_max = result[-1]
    permutation_max = permutation
# runcode(x)
print(result_max)
print(permutation_max)

# runcode(x, [5, 64])