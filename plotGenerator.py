import matplotlib.pyplot as plt

with open('../moleResults/cache-thrash16size.txt', 'r') as f:
  header = f.readline().strip().replace(' ','').upper().split('\t')
#  print(header)
  array = []
  for i in range(len(header)):
    array.append([])
#  print array
  for line in f:
    #array.append(line.strip().split('\t'))
    data = line.strip().split('\t')
    for i in range(len(data)):
      array[i].append(float(data[i]))

# print array

plt.plot(array[0], array[1], '--ro')
plt.plot(array[0], array[2], '--yo')
plt.plot(array[0], array[3], '--bo')


plt.axis([min(array[0]), max(array[0]), min(array[1] + array[2] + array[3]), 
                                        max(array[1] + array[2] + array[3])])
plt.show()

