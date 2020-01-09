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
# x ='''deal with increment 5'''
lines = x.splitlines()

# adapted from pseudocode from https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
def modInverse(a, n):
  t = 0
  new_t = 1
  r = n
  new_r = a
  while new_r != 0:
    q = r // new_r
    (t, new_t) = (new_t, t - q * new_t)
    (r, new_r) = (new_r, r - q * new_r)
  if r > 1:
    return 'a is not invertible'
  if t < 0:
    t = t + n
  return t

# explanation from https://dhconnelly.com/advent-of-code-2019-commentary.html#day-22
# adapted from https://topaz.github.io/paste/#XQAAAQAgBQAAAAAAAAAzHIoib6pENkSmUIKIED8dy140D1lKWSMhNhZz+hjKgIgfJKPuwdqIBP14lxcYH/qI+6TyUGZUnsGhS4MQYaEtf9B1X3qIIO2JSejFjoJr8N1aCyeeRSnm53tWsBtER8F61O2YFrnp7zwG7y303D8WR4V0eGFqtDhF/vcF1cQdZLdxi/WhfyXZuWC+hs8WQCBmEtuId6/G0PeMA1Fr78xXt96Um/CIiLCievFE2XuRMAcBDB5We73jvDO95Cjg0CF2xgF4yt3v4RB9hmxa+gmt6t7wRI4vUIGoD8kX2k65BtmhZ7zSZk1Hh5p1obGZ6nuuFIHS7FpuSuv1faQW/FuXlcVmhJipxi37mvPNnroYrDM3PFeMw/2THdpUwlNQj0EDsslC7eSncZQPVBhPAHfYojh/LlqSf4DrfsM926hSS9Fdjarb9xBYjByQpAxLDcmDCMRFH5hkmLYTYDVguXbOCHcY+TFbl+G/37emZRFh/d+SkeGqbFSf64HJToM2I7N2zMrWP7NDDY5FWehD5gzKsJpEg34+sG7x2O82wO39qBlYHcYg1Gz4cLBrH1K1P+KWvEdcdj/NBtrl6yftMlCu6pH4WTGUe9oidaiRuQZOGtw71QsTQUuhpdoWO4mEH0U9+CiPZCZLaQolFDSky1J9nDhZZHy3+ETcUeDOfSu+HI3WuKC0AtIRPdG8B9GhtxZQKAx+5kyi/ek7A2JAY9SjrTuvRADxx5AikbHWXIsegZQkupAc2msammSkwY8dRMk0ilf5vh6kR0jHNbSi0g0KJLCJfqggeX24fKk5Mdh8ULZXnMfMZOmwEGfegByYbu91faLijfW4hoXCB1nlsWTPZEw2PCZqqhl9oc1q25H2YkkvKLxEZWl6a9eFuRzxhB840I1zdBjUVgfKd9/V4VdodzU2Z2e+VEh7RbJjQNFC/rG8dg==
def merged_scale_and_shift(lines, reverse, start, initial_scale = 1, initial_shift = 0):
  merged_scale = initial_scale
  merged_shift = initial_shift
  for line in lines:
    if line == 'deal into new stack':
      start = (-start - 1) % size
      scale = -1
      shift = -1
    elif line.startswith('cut '):
      count = int(line.strip('cut '))
      if reverse:
        start = (start + count) % size
        scale = 1
        shift = count
      else:
        start = (start - count) % size
        scale = 1
        shift = -count
    elif line.startswith('deal with increment '):
      count = int(line.strip('deal with increment '))
      if reverse:
        # inverse = count ** (size-2) % size # see method 3 of https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
        inverse = modInverse(count, size)
        start = (start * inverse) % size
        scale = inverse
        shift = 0
      else:
        start = (start * count) % size
        scale = count
        shift = 0
    merged_scale = (scale * merged_scale) % size # If k a ≡ k b (mod n) and k is coprime with n, then a ≡ b (mod n)
    merged_shift = (scale * merged_shift + shift) % size
  return (merged_scale, merged_shift, start)

reverse = False
if reverse:
  lines.reverse()
size = 119315717514047
# size = 10007
# start = 4758978110959
real_start = 2020
start = real_start
end = -1
i = 0
times = 101741582076661
# times = 5
merged_scale = 1
merged_shift = 0
# for i in range(times):
#   # (merged_scale, merged_shift, end) = merged_scale_and_shift(lines, reverse, start)
#   (merged_scale, merged_shift, end) = merged_scale_and_shift(lines, reverse, start, merged_scale, merged_shift)
#   print(f'i {i} start {start} end {end} = ({merged_scale} * {real_start} + {merged_shift}) % {size} = {(merged_scale * real_start + merged_shift) % size}')
#   start = end

(merged_scale, merged_shift, end) = merged_scale_and_shift(lines, reverse, start)
repeated_scale = pow(merged_scale, times, size)
repeated_shift = merged_shift * (repeated_scale - 1) * modInverse(merged_scale - 1, size) % size
repeated_end = (repeated_scale * real_start + repeated_shift) % size
reversed_repeated_end = ((real_start - repeated_shift) * modInverse(repeated_scale, size)) % size
print(f'repeated_scale {repeated_scale} repeated_shift {repeated_shift} repeated_end {repeated_end} reversed_repeated_end {reversed_repeated_end}')
# ans 45347150615590
# repeated_scale 80484954784936 repeated_shift 49323001031774 repeated_end 1608694956433 reversed_repeated_end 45347150615590