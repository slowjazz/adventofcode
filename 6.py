inp = """
63, 142
190, 296
132, 194
135, 197
327, 292
144, 174
103, 173
141, 317
265, 58
344, 50
184, 238
119, 61
329, 106
70, 242
272, 346
312, 166
283, 351
286, 206
57, 225
347, 125
152, 186
131, 162
45, 299
142, 102
61, 100
111, 218
73, 266
350, 173
306, 221
42, 284
150, 122
322, 286
346, 273
75, 354
68, 124
194, 52
92, 44
77, 98
77, 107
141, 283
87, 306
184, 110
318, 343
330, 196
303, 353
268, 245
180, 220
342, 337
127, 107
203, 127
"""

data = [data.split(',') for data in inp.splitlines()[1:]]
xcoords = [int(d[0]) for d in data]
ycoords = [int(d[1]) for d in data]
data = list(zip(xcoords, ycoords))
print(data)

minX,maxX, minY, maxY = min(xcoords), max(xcoords), min(ycoords), max(ycoords)

board = [[0 for x in range(400)] for y in range(400)]

def md(a, b):
	return abs(b[0]-a[0]) + abs(b[1]-a[1])

def getClosest(point):
	# return index of data corresponding to closest point, and 0 if tie
	dists = []
	for j in range(len(data)):
		dists.append((md(point, data[j]), j))
	dists = sorted(dists, key=lambda x: x[0])

	# print(point, data[dists[0][1]], dists)

	if (dists[0][0] != dists[1][0]):
		return dists[0][1] +1
	else: return 0

def getAllDist(point):
	dists = 0
	for j in range(len(data)):
		dists += md(point, data[j])
	if dists <10000:
		return 1
	else: return 0

for i in range(len(board)):
	for j in range(len(board[0])):
		#board[j][i] = getClosest((i,j))
		board[j][i] = getAllDist((i,j))

flat_list = [item for sublist in board for item in sublist]

from collections import Counter
print(Counter(flat_list))
#print([x[minX:maxX+1] for x in board[minY:maxY+1]])
#print([x[:16] for x in board[:16]])


