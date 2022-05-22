import random
from itertools import permutations, combinations
from math import factorial
import matplotlib.pyplot as plt
from time import time as timer

starttime = timer()

npoints = 7         # max 15 for <1s computation

class Point:
  
  def __init__(self, xpos, ypos, line='A'):
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
# Consider some method where we guarantee paths will not cross, which might necessarily? Be less efficient
#nodesA = [Point(i,j,'A') for i,j in zip(x,y) if x.index(i) <= int(npoints/2)]    # int ensures that one
#nodesB = [Point(i,j,'B') for i,j in zip(x,y) if x.index(i) >= int(npoints/2)]    # node is shared
# WARNING: the above block causes an error ONLY if a value should appear in both lists
# this is because x.index(i) outputs ONLY the lowest index for a repeat value
# e.g. if x[1] and x[12] both = 42, then x.index(42) = 12

# Use n*n array to store distances between points?

#nodesA = [Point(x[i], y[i], 'A') for i in range(int(npoints/2)+1)]
#nodesB = [Point(x[i], y[i], 'B') for i in range(int(npoints/2), npoints)]

nodes = [Point(x[i], y[i]) for i in range(npoints)]

pathsB = [None for i in range(2,npoints)]      # Each element of combosB is a list nCi
pathsA = [None for i in range(2,npoints)]      # Each element of each nCi is a tuple
                                               # of i nodes
# Consider defining a function to facilitate pairing relevant combinations

lengthsA = [None for i in range(2, npoints)]
lengthsB = [None for i in range(2, npoints)]

for i in range(2, npoints):
  pathsB[i-2] = list(permutations(nodes, i))
  pathsA[i-2] = list(permutations(nodes, i))
  lengthsA[i-2] = [0 for j in pathsA[i-2]]
  lengthsB[i-2] = [0 for j in pathsB[i-2]]

#pathsA[0][0][0].line = 'B'                               # Sanity check
#print(pathsA[0][0][0].line, pathsB[0][0][0].line)

# Each pathsA[i][j][k] is the kth node of the jth permutation of i nodes.
# Each lengthsA[i][j] is the path length of the jth permutation of i nodes.
# Some way to delete permutations that are mirrors of each other?

# Want best such that A union B = nodes.

#nodesA[-1].both = True
#nodesB[0].both = True
#print(nodesA[-1].xpos, nodesB[0].xpos)

#for i in range(npoints):
#  print(x[i],y[i])
#  print(nodes[i].xpos,nodes[i].ypos)

for i in range(len(lengthsA)):
  for j in range(len(lengthsA[i])):
    #print(len(pathsA[i][j]), len(pathsB[i][j]))   # Sanity check
    for k in range(len(pathsA[i][j])-1):
      lengthsA[i][j] += distcalc(pathsA[i][j][k], pathsA[i][j][k+1])
      lengthsB[i][j] += distcalc(pathsB[i][j][k], pathsB[i][j][k+1])
# Several unnecessary calc: did same things for pathsA and B, lengths A and B,
# could just declare and assign later.

# pathsA[0] should match with pathsB[-1] ?
lengths = []
trackpath = []

for i in range(len(pathsA)):
  for j in range(len(pathsA[i])):
    for k in range(len(pathsB[-1-i])):
      if set(pathsA[i][j]).union(set(pathsB[-1-i][k])) == set(nodes):
        lengths.append(lengthsA[i][j] + lengthsB[-1-i][k])
        trackpath.append([pathsA[i][j], pathsB[-1-i][k]])
      #  union = True
      #else: union = False
      #if len(set(pathsA[i][j]).intersection(set(pathsB[-1-i][k]))) == 1:
      #  intersection = True
      #else: intersection = False
      #if union != intersection: print('bad')
        # Use dict to track indices?
        #print('yes',i,j,k)
      #else: print('no',i,j,k)
print(len(lengths)) 
print(min(lengths), max(lengths))
print(len(set(lengths)))
''' Something is very wrong here (I think just the test is bad)
duplicates = 0
for i in range(len(lengths)):
  for j in range(i):
    if i==j:
      continue
    elif lengths[i]==lengths[j]:
      duplicates += 1
      print(i,j,lengths[i], lengths[j],duplicates, len(lengths))
print(duplicates)
'''
#for i in range(len(lengthsA)):
#  for j in range(len(lengthsA[i])):
#    print(i,j,lengthsA[i][j])
#    if i==5: quit('0')
endtime = timer()

print('computation time =', endtime-starttime, 'seconds')

best = lengths.index(min(lengths))
xa = [i.xpos for i in trackpath[best][0]]
ya = [i.ypos for i in trackpath[best][0]]
xb = [i.xpos for i in trackpath[best][1]]
yb = [i.ypos for i in trackpath[best][1]]
plt.plot(xa,ya,'+-')
plt.plot(xb,yb,'+-')
plt.axis('equal')
#fig, ax = plt.plot()
#ax.plot(xa,ya,'+-')
#ax.plot(xb,yb,'+-')
#ax.axis('equal')
plt.show()
quit('0')

#for i in range(len(pathsA)):
#  for j in range(len(nodesA)-1):
#    lengthsA[i] += distcalc(pathsA[i][j], pathsA[i][j+1])
#for i in range(len(pathsB)):
#  for j in range(len(nodesB)-1):
#    lengthsB[i] += distcalc(pathsB[i][j], pathsB[i][j+1])
      
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
