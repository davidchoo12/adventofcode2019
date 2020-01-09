def runcode(code_str, inputs=[]):
  # print(f'runcode called with inputs: {inputs}')
  x = list(map(int, code_str.split(',')))
  x += [0] * 10 * len(x)
  inputsi = 0
  i = 0
  returnvalue = 0
  relative_base = 0
  while i < len(x):
    op = x[i] % 100
    if op == 99:
      # print('exiting runcode')
      return [0, returnvalue]
    mode1 = int(x[i] / 100 % 10)
    param1 = x[x[i+1]] if mode1 == 0 else x[i+1] if mode1 == 1 else x[relative_base + x[i+1]]
    if op == 3:
      # print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      if not inputs: # if inputs not specified
        if mode1 == 2:
          x[relative_base + x[i+1]] = int(input())
        else:
          x[x[i+1]] = int(input())
        # print(f'input {x[x[i+1]]}', end = ' |')
      elif inputsi < len(inputs): # if not yet finish reading inputs
        if mode1 == 2:
          x[relative_base + x[i+1]] = inputs[inputsi]
        else:
          x[x[i+1]] = inputs[inputsi]
        # print(f'input {x[x[i+1]]}', end = ' |')
        inputsi += 1
      else:
        # print('exiting runcode (inputs cleared)')
        return [1, returnvalue]
      i += 2
    elif op == 4:
      # print(f'{x[i]}, {mode1}:{param1}', end = ' |')
      print(f'output {param1}')
      returnvalue = param1
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

runcode(code)