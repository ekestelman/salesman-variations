import random
from itertools import permutations
from math import factorial
import matplotlib.pyplot as plt
from time import time as timer

starttime = timer()

npoints = 8         # max 15 for <1s computation

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

# Consider placing intersection node in middle of optimized path rather than randomly
#nodesA = [Point(i,j,'A') for i,j in zip(x,y) if x.index(i) <= int(npoints/2)]    # int ensures that one
#nodesB = [Point(i,j,'B') for i,j in zip(x,y) if x.index(i) >= int(npoints/2)]    # node is shared
# WARNING: the above block causes an error ONLY if a value should appear in both lists
# this is because x.index(i) outputs ONLY the lowest index for a repeat value
# e.g. if x[1] and x[12] both = 42, then x.index(42) = 12

# Use n*n array to store distances between points?

nodesA = [Point(x[i], y[i], 'A') for i in range(int(npoints/2)+1)]
nodesB = [Point(x[i], y[i], 'B') for i in range(int(npoints/2), npoints)]

#print(x,'\n',y)
#print(len(nodesA),len(nodesB))

#for i,j in zip(nodesA, nodesB):
#  print(i.xpos, j.xpos)

nodesA[-1].both = True
nodesB[0].both = True
#print(nodesA[-1].xpos, nodesB[0].xpos)

#quit(0)

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

# store dist from intersection to other nodes

avgDistA = 0
avgDistB = 0
distToHubA = [0 for i in range(len(nodesA))]
distToHubB = [0 for i in range(len(nodesB))]
segmentsA = [None for i in range(len(nodesA)-1)]
segmentsB = [None for i in range(len(nodesB)-1)]

for i in range(len(nodesA)-1):
  segmentsA[i] = distcalc(pathsA[bestpathA][i], pathsA[bestpathA][i+1])

for i in range(len(nodesB)-1):
  segmentsB[i] = distcalc(pathsB[bestpathB][i], pathsB[bestpathB][i+1])

#for i in range(len(nodesA)-1, 0, -1):               # nodesA[-1] is the hub... this won't work
#  distToHubA[i] = distToHubA[i-1] + segmentsA[i]

#i = pathsA[bestpathA].index(j) if j.both==True
for i in pathsA[bestpathA]:
  if i.both:
    hubA = pathsA[bestpathA].index(i)

for i in range(hubA-1, -1, -1):
  distToHubA[i] = distToHubA[i+1] + segmentsA[i]

for i in range(hubA+1, len(nodesA)):
  distToHubA[i] = distToHubA[i-1] + segmentsA[i-1]

print(distToHubA)

for i in pathsB[bestpathB]:
  if i.both:
    hubB = pathsB[bestpathB].index(i)

for i in range(hubB-1, -1, -1):
  distToHubB[i] = distToHubB[i+1] + segmentsB[i]

for i in range(hubB+1, len(nodesB)):
  distToHubB[i] = distToHubB[i-1] + segmentsB[i-1]

print(distToHubB)

avgAcross = sum(distToHubA) / (len(distToHubA)-1) + sum(distToHubB) / (len(distToHubB)-1)
# Average distane between a point on path A and a point on path B, crossing from
# one path to the other at the hub node.
# -1 to exclude hub iself

print(avgAcross)

#while not pathsA[bestpathA][i].both:
#  distToHub[i] = 0

# Did some algebra for this

for i in range(len(nodesA)-1):
  avgDistA += i * distcalc(pathsA[bestpathA][i], pathsA[bestpathA][i+1]) * (len(nodesA) - i)
for i in range(len(nodesB)-1):
  avgDistB += i * distcalc(pathsB[bestpathB][i], pathsB[bestpathB][i+1]) * (len(nodesB) - i)

avgDistA /= (len(nodesA)**2 - len(nodesA)) / 2
avgDistB /= (len(nodesB)**2 - len(nodesB)) / 2

print(avgDistA, avgDistB)

print( (len(nodesA)**2 - len(nodesA))/2 + (len(nodesB)**2 - len(nodesB))/2 + \
  (len(distToHubA)-1) * (len(distToHubB)-1) )
print( (npoints**2 - npoints)/2 )
# Confirming some math

# When averaging across the two averages, be careful of repeat points (the hub) and weights

avgDist = (avgAcross * (len(distToHubA)-1) * (len(distToHubB)-1) + \
  avgDistA * (len(nodesA)**2 - len(nodesA)) / 2 + avgDistB * (len(nodesB)**2 - len(nodesB)) / 2) \
  / ((npoints**2 - npoints) / 2)

print('average distance between points =', avgDist)

lengths = [i+j for i,j in zip(lengthsA,lengthsB)]

endtime = timer()

print('computation time =', endtime-starttime, 'seconds')

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(xa, ya, '+-')
ax1.plot(xb, yb, '+-')
ax2.hist(lengths, bins=int(npoints/2*(npoints/2-2)), ec='black')
#plt.plot(x, y, '+-')
#pl.show()
#plt.hist(lengths)
plt.show()
