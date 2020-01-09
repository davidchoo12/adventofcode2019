sum = 0
for i in range(138307, 654504):
  noDesc = True
  adjEq = False
  l = 0
  for k in [int(j) for j in str(i)]:
    if k < l:
      noDesc = False
      break
    if k == l:
      adjEq = True
    l = k
  if noDesc and adjEq:
    sum += 1
print(sum)