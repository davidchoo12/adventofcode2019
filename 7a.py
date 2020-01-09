x = '3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99'
x = list(map(int, x.split(',')))

def runcode(x, inputs):
  inputsi = 0
  i = 0
  returnvalue = 0
  while i < len(x):
    op = x[i] % 100
    if op == 99:
      print('exiting runcode')
      return returnvalue
    mode1 = int(x[i] / 100 % 10)
    param1 = x[i+1] if mode1 else x[x[i+1]]
    if op == 3:
      print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      x[x[i+1]] = inputs[inputsi]
      print(f'input {inputs[inputsi]}', end = ' |')
      inputsi += 1
      i += 2
    elif op == 4:
      print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      print(x[x[i+1]])
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

outpipe_max = 0

for permutation in permutations(list(range(4))):
  outpipe = 0
  for phase in permutation:
    outpipe = runcode(x, [phase, outpipe])
  print(f'permutation: {permutation}, outpipe: {outpipe}')
  if (outpipe > outpipe_max):
    outpipe_max = outpipe
    permutation_max = permutation

print(outpipe_max)
print(permutation_max)

# runcode(x, [0, 1])