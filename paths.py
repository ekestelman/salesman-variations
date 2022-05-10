import random
from itertools import permutations
from math import factorial
import matplotlib.pyplot as plt
from time import time as timer

starttime = timer()

npoints = 8

class Point:
  
  def __init__(self, xpos, ypos):
    self.xpos = xpos
    self.ypos = ypos
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

nodes = [Point(i,j) for i,j in zip(x,y)]

#for i in range(npoints):
#  print(x[i],y[i])
#  print(nodes[i].xpos,nodes[i].ypos)

lengths = [0 for i in range(factorial(npoints))]
#lengths = [[0 for i in range(factorial(npoints-1))] for j in range(npoints)]
paths = list(permutations(nodes))

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

for i in range(len(paths)):
  for j in range(npoints-1):
    lengths[i] += distcalc(paths[i][j], paths[i][j+1])
      
#pathlength = {i: j for i,j in zip(lengths, paths)}
#print(paths)
#print(lengths)
#print(len(paths),len(lengths))
bestpath = lengths.index(min(lengths))
#print(bestpath)
print('length of shortest path =', lengths[bestpath])
 
x = [i.xpos for i in paths[bestpath]]
y = [i.ypos for i in paths[bestpath]]

avgDist = 0                   # Initialize avg distance between points along path

for i in range(npoints-1):                    # Did some algebra for this
  avgDist += i * distcalc(paths[bestpath][i], paths[bestpath][i+1]) * (npoints - i)

avgDist /= (npoints**2 - npoints) / 2      # npoints choose 2

print('average distance along path between any two points =', avgDist)

#for i in paths[bestpath]:
#  for j in paths[bestpath]:
#    avgDist += distcalc     # Want dist along path, not Euclidean distance

endtime = timer()

print('computation time =', endtime-starttime, 'seconds')

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(x, y, '+-')
ax2.hist(lengths, bins=npoints*(npoints-2), ec='black')
#plt.plot(x, y, '+-')
#pl.show()
#plt.hist(lengths)
plt.show()
