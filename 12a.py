import re

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
  print(f'pos {pos}')
  print(f'vel {vel}')

for i in range(1000):
  print(f'step {i}')
  step()
  potential_energy = [sum([abs(k) for k in p]) for p in pos]
  kinetic_energy = [sum([abs(k) for k in v]) for v in vel]
  total_energy = sum([p * kinetic_energy[i] for i, p in enumerate(potential_energy)])
  print(f'pot {potential_energy}')
  print(f'kin {kinetic_energy}')
  print(f'sum {total_energy}')
