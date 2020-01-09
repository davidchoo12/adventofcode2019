sum = 0
for i in range(138307, 654504):
  noDesc = True
  adjFound = False
  adjCount = 0
  l = 0
  for k in [int(j) for j in str(i)]:
    if k < l:
      noDesc = False
      break
    if k == l:
      adjCount += 1
    else:
      if adjCount == 1:
        adjFound = True
      adjCount = 0
    l = k
  if adjCount == 1:
    adjFound = True
  if noDesc and adjFound:
    sum += 1
print(sum)