import matplotlib.pyplot as plt

with open('../moleResults/cache-thrash16size.txt', 'r') as f:
  array = []
  for line in f:
    array.append(line.strip().split('\t'))

for line in array:
  print line

# plt.plot([1,2,3,4], [1,4,9,16], '--ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

