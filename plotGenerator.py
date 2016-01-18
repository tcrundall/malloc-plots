#!/usr/bin/env python
import re
import argparse

from pylab import *
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--benchmark', dest='benchmark', help='name of desired benchmark')
parser.add_argument('-t', '--threads',   dest='threads',   help='number of threads')
parser.add_argument('-s', '--size',      dest='size',      help='size of objects')

args = parser.parse_args()

# INSERT IF STATEMENTS HERE!!!!
successful = False
benchMachine = "mole"

try:
# looking for a size.txt file
  if args.threads is None:
    with open('../'+benchMachine+'Results/'+str(args.benchmark)+str(args.size)+'size.txt', 'r') as f:
      successful = True
      header = f.readline().strip().replace(' ','').upper().split('\t')
      array = []
      for i in range(len(header)):
	array.append([])
      
      for line in f:
	data = line.strip().split('\t')
	for i in range(len(data)):
	  array[i].append(float(data[i]))

      plt.title(str(args.benchmark).capitalize()+' on '+benchMachine.capitalize()+\
                ' Architecture with Object Size '+str(args.size))
      plt.xlabel('thread count')
  # looking for a thread.txt file
  if args.size is None:
    with open('../'+benchMachine+'Results/'+str(args.benchmark)+str(args.threads)+'threads.txt', 'r') as f:
      header = f.readline().strip().replace(' ','').upper().split('\t')
      array = []
      for i in range(len(header)):
	array.append([])
      for line in f:
	data = line.strip().split('\t')
	for i in range(len(data)):
	  array[i].append(float(data[i]))
      plt.title(str(args.benchmark).capitalize()+' on '+benchMachine.capitalize()+\
                ' Architecture with Thread Count '+str(args.threads))
      plt.xlabel('object size')

  plt.ylabel('time (s)') 
  plt.plot(array[0], array[1], '--ro', label='glib')
  plt.plot(array[0], array[2], '--yo', label='Hoard')
  plt.plot(array[0], array[3], '--bo', label='tcMalloc')

  legend()

  plt.axis([min(array[0]), max(array[0]), min(array[1] + array[2] + array[3]), 
					  max(array[1] + array[2] + array[3])])
  plt.savefig(str(args.benchmark)+benchMachine.capitalize())
  plt.show()
except IOError:
  pass
