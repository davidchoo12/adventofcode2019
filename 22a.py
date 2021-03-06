x = '''deal with increment 61
cut 7724
deal into new stack
cut -7151
deal with increment 22
deal into new stack
deal with increment 11
cut -2506
deal with increment 14
cut 9670
deal with increment 59
cut 3341
deal into new stack
cut 9816
deal with increment 3
cut -7547
deal with increment 31
cut 7178
deal into new stack
deal with increment 52
deal into new stack
deal with increment 70
cut 3702
deal with increment 62
cut -6554
deal with increment 68
cut 1356
deal with increment 58
cut -9486
deal with increment 5
cut 3969
deal into new stack
deal with increment 9
cut 1376
deal with increment 70
cut 4921
deal with increment 38
deal into new stack
cut -4708
deal with increment 56
deal into new stack
cut 6672
deal with increment 53
cut -6567
deal with increment 28
cut -6494
deal with increment 57
deal into new stack
cut 3002
deal with increment 53
cut 5450
deal with increment 5
cut 7672
deal with increment 63
cut -9864
deal with increment 66
cut 5734
deal with increment 23
cut 9172
deal with increment 8
cut 3219
deal with increment 49
cut -975
deal with increment 52
deal into new stack
deal with increment 10
cut 6050
deal with increment 68
deal into new stack
cut -3778
deal with increment 25
cut 9259
deal with increment 41
cut -268
deal with increment 44
deal into new stack
cut -1431
deal with increment 48
cut -1885
deal with increment 75
cut 8570
deal with increment 49
deal into new stack
deal with increment 62
deal into new stack
deal with increment 35
deal into new stack
deal with increment 30
cut -3800
deal with increment 4
deal into new stack
deal with increment 27
cut 2827
deal with increment 2
cut -2346
deal with increment 19
cut 6615
deal with increment 38
cut 2739
deal into new stack'''
lines = x.splitlines()
size = 10007
hand = [i for i in range(size)]

for line in lines:
  if line == 'deal into new stack':
    print('n')
    hand.reverse()
  elif line.startswith('cut '):
    count = int(line.strip('cut '))
    print(f'c {count}')
    hand = hand[count:] + hand[0:count]
  elif line.startswith('deal with increment '):
    count = int(line.strip('deal with increment '))
    print(f'd {count}')
    newhand = [0] * size
    i = 0
    while hand:
      front = hand.pop(0)
      newhand[i % size] = front
      i += count
    hand = newhand
    # print(hand)
print(hand.index(2019))
# ans 2939