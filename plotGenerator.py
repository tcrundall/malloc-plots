import matplotlib.pyplot as plt

with open('../moleResults/cache-thrash16size.txt', 'r') as f:
  array = []
  for line in f:
    array.append(line.strip().split('\t'))



print array[0]
for i in range(len(array[0])) :
  array[0][i] = array[0][i].strip().upper()

for i in range(1, len(array)):
  for j in range(len(array[0])):
    array[i][j] = float(array[i][j])

print "here"

for line in array:
  print line


plt.plot([1,2,3,4,5,6,7,8], [array[1][1],array[2][1],array[3][1],array[4][1],array[5][1],array[6][1],array[7][1],array[8][1]], '--ro')

plt.plot([1,2,3,4,5,6,7,8], [array[1][2],array[2][2],array[3][2],array[4][2],array[5][2],array[6][2],array[7][2],array[8][2]], '--yo')

plt.plot([1,2,3,4,5,6,7,8], [array[1][3],array[2][3],array[3][3],array[4][3],array[5][3],array[6][3],array[7][3],array[8][3]], '--bo')



plt.axis([1, 8, 0, 7])
plt.show()

