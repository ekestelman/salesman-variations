import random
from itertools import permutations
from math import factorial
import matplotlib.pyplot as plt
from time import time as timer

starttime = timer()

npoints = 8

class Point:
  
  def __init__(self, xpos, ypos, line):
    self.xpos = xpos
    self.ypos = ypos
    self.line = line             # Which line does this point belong to
    self.both = False            # Point belongs on both lines
    #self.neighbors = []

class Path:

  def __init__(self, nodes):
    self.segment = [0 for i in nodes-1]
    self.total = sum(self.segment)         # check syntax

#class Path:
#  
#  def __init__(self, 

def distcalc(a, b):
  return ( (a.xpos - b.xpos) ** 2 + (a.ypos - b.ypos) ** 2 ) ** 0.5

x = [random.randrange(0,101) for i in range(npoints)]
#x = np.random.randint(100, size=npoints)

y = [random.randrange(0,101) for i in range(npoints)]

#nodes = [Point(i,j,'A') for i,j in zip(x,y)]

nodesA = [Point(i,j,'A') for i,j in zip(x,y) if x.index(i) <= int(npoints/2)]    # int ensures that one
nodesB = [Point(i,j,'B') for i,j in zip(x,y) if x.index(i) >= int(npoints/2)]    # node is shared

#for i in range(npoints):
#  print(x[i],y[i])
#  print(nodes[i].xpos,nodes[i].ypos)

lengthsA = [0 for i in range(factorial(len(nodesA)))]
lengthsB = [0 for i in range(factorial(len(nodesB)))]
#lengths = [[0 for i in range(factorial(npoints-1))] for j in range(npoints)]
pathsA = list(permutations(nodesA))
pathsB = list(permutations(nodesB))

#pathlength = {i: j for i,j in zip(lengths, paths)} # Use pointers to keep order and change vals?
#print(pathlength)

#for i in range(npoints):                # Bad block?
#  for j in range(npoints):
#    if i==j:
#      continue
#    else:
#      lengths[i] += distcalc(nodes[i], nodes[j])
#      #dist[i][j] = ( (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 ) ** 0.5

#for i in range(npoints-1):                     # There is 1 fewer edge than there are nodes
#  lengths[i] += distcalc(nodes[i], nodes[i+1])
#  for j in range(factorial(npoints)): #maybe need a while loop?
#    for k in range(npoints):

for i in range(len(pathsA)):
  for j in range(len(nodesA)-1):
    lengthsA[i] += distcalc(pathsA[i][j], pathsA[i][j+1])
for i in range(len(pathsB)):
  for j in range(len(nodesB)-1):
    lengthsB[i] += distcalc(pathsB[i][j], pathsB[i][j+1])
      
#pathlength = {i: j for i,j in zip(lengths, paths)}
#print(paths)
#print(lengths)
#print(len(paths),len(lengths))
bestpathA = lengthsA.index(min(lengthsA))
bestpathB = lengthsB.index(min(lengthsB))
#print(bestpath)
print('length of shortest path A =', lengthsA[bestpathA])
print('length of shortest path B =', lengthsB[bestpathB])
print('total =', lengthsA[bestpathA]+lengthsB[bestpathB])
 
xa = [i.xpos for i in pathsA[bestpathA]]
ya = [i.ypos for i in pathsA[bestpathA]]
xb = [i.xpos for i in pathsB[bestpathB]]
yb = [i.ypos for i in pathsB[bestpathB]]


endtime = timer()

print('computation time =', endtime-starttime, 'seconds')

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(xa, ya, '+-')
ax1.plot(xb, yb, '+-')
#ax2.hist(lengths, bins=npoints*(npoints-2), ec='black')
#plt.plot(x, y, '+-')
#pl.show()
#plt.hist(lengths)
plt.show()
