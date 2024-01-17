def maxmin(array):
  x = sorted(array)
  return [x[0], x[-1]]


a = [2, 4, 1, 0, 2, -1]
b = [20, 50, 12, 6, 14, 8]
c = [100, -100]

print(maxmin(a))
print(maxmin(b))
print(maxmin(c))