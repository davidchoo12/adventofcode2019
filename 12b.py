import re
import math

# first example
text = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''
# second example
text = '''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''
# actual
text = '''<x=13, y=9, z=5>
<x=8, y=14, z=-2>
<x=-5, y=4, z=11>
<x=2, y=-6, z=1>'''
orig_pos = [[int(p) for p in re.findall(r'-?\d+', line)] for line in text.splitlines()]
pos = [[int(p) for p in re.findall(r'-?\d+', line)] for line in text.splitlines()]
# pos = [[13, 9, 5],
#       [8, 14, -2],
#       [-5, 4, 11],
#       [2, -6, 1]]
print(f'pos {pos}')
vel = [[0,0,0] for x in pos]

def update_vel():
  for i, curr_pos in enumerate(pos):
    for other_pos in pos:
      for j in range(3):
        vel[i][j] += 1 if other_pos[j] > curr_pos[j] else -1 if other_pos[j] < curr_pos[j] else 0
def update_pos():
  for i in range(len(pos)):
    for j in range(3):
      pos[i][j] += vel[i][j]

def step():
  update_vel()
  update_pos()
  # print(f'pos {pos}')
  print(f'vel {vel}')

print(f'step 1')
step()
i = 1
# while pos != orig_pos:
# print([not v[0] for v in vel])
# find no of steps until velocity is 0 again for each axis
# when all velocity is 0, its the midpoint before going back to original position
found = [0, 0, 0]
found = [found[xyz] if found[xyz] else i if not any([v[xyz] for v in vel]) else 0 for xyz in range(3)]
print(f'found {found}')
while not all(found):
  print(f'step {i+1}')
  step()
  i += 1
  found = [found[xyz] if found[xyz] else i if not any([v[xyz] for v in vel]) else 0 for xyz in range(3)]
  print(f'found {found}')

# ans = 1
# for f in found:
#   ans *= f
  # potential_energy = [sum([abs(k) for k in p]) for p in pos]
  # kinetic_energy = [sum([abs(k) for k in v]) for v in vel]
  # total_energy = sum([p * kinetic_energy[i] for i, p in enumerate(potential_energy)])
  # print(f'pot {potential_energy}')
  # print(f'kin {kinetic_energy}')
  # print(f'sum {total_energy}')

# print(i)
ans = 1
# find least common multiple of found
for f in found:
  gcd = math.gcd(ans, f)
  # print(gcd)
  ans *= f
  # print(ans)
  ans //= gcd
  # print(ans)
# print(math.gcd(found[0], found[1]))
# print(math.gcd(found[0], found[2]))
# print(math.gcd(found[1], found[2]))
print(ans * 2)