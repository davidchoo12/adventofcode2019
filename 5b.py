x = '3,225,1,225,6,6,1100,1,238,225,104,0,1001,210,88,224,101,-143,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,101,42,92,224,101,-78,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1101,73,10,225,1102,38,21,225,1102,62,32,225,1,218,61,224,1001,224,-132,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,19,36,225,102,79,65,224,101,-4898,224,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1101,66,56,224,1001,224,-122,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1002,58,82,224,101,-820,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,2,206,214,224,1001,224,-648,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,76,56,224,1001,224,-4256,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,37,8,225,1101,82,55,225,1102,76,81,225,1101,10,94,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1107,677,677,224,1002,223,2,223,1006,224,389,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,404,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,419,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,8,226,226,224,1002,223,2,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,524,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,554,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,569,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,584,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,599,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,629,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,659,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226'
x = list(map(int, x.split(',')))
i = 0
while i < len(x):
  op = x[i] % 100
  if op == 99: break
  mode1 = int(x[i] / 100 % 10)
  param1 = x[i+1] if mode1 else x[x[i+1]]
  if op == 3:
    print(f'{x[i]}, {mode1}:{param1}')
    x[x[i+1]] = 5
    # print('input 1')
    i += 2
  elif op == 4:
    print(f'{x[i]}, {mode1}:{param1}')
    print(x[x[i+1]])
    i += 2
  else:
    mode2 = int(x[i] / 1000 % 10)
    param2 = x[i+2] if mode2 else x[x[i+2]]
    if op == 5:
      print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}')
      if param1:
        i = param2
      else:
        i += 3
    elif op == 6:
      print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}')
      if not param1:
        i = param2
      else:
        i += 3
    else:
      mode3 = int(x[i] / 10000 % 10)
      param3 = x[i+3] if mode3 else x[x[i+3]]
      if op == 1:
        print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}')
        x[x[i+3]] = param1 + param2
        i += 4
      elif op == 2:
        print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}')
        x[x[i+3]] = param1 * param2
        i += 4
      elif op == 7:
        print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}')
        x[x[i+3]] = 1 if param1 < param2 else 0
        i += 4
      elif op == 8:
        print(f'{x[i]}, {mode1}:{param1}, {mode2}:{param2}, {mode3}:{param3}')
        x[x[i+3]] = 1 if param1 == param2 else 0
        i += 4
# for i in range(len(x))
# for i in range(0, len(x), 4):
#   if (x[i] == 99): break
#   if (x[i] == 1): x[x[i+3]] = x[x[i+1]] + x[x[i+2]]
#   elif (x[i] == 2): x[x[i+3]] = x[x[i+1]] * x[x[i+2]]

# print(x)
