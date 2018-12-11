inp = "1718"

grid = [[0 for x in range(300)] for y in range(300)]
cache = [[0 for x in range(300)] for y in range(300)]
temp = [[0 for x in range(300)] for y in range(300)]
for y in range(len(grid)):
	for x in range(len(grid)):
		rid = x+10
		plvl = rid*y
		plvl += int(inp)
		plvl *= rid
		grid[y][x] = int(str(plvl)[-3]) - 5
		cache[y][x] = int(str(plvl)[-3]) - 5
res = float('-inf')
resInd = 0
lastSize = 0
for k in range(1,301):
	print(k)
	for i in range(len(grid)-k):
		for j in range(len(grid)-k):

			s = cache[j][i] 
			s += sum(grid[i+k-1][j:j+k])
			s += sum([grid[i+p][j+k-1] for p in range(k-1)])
			if  s> res:
				res = s
				resInd = (j,i, k)
			temp[j][i] = s
	cache = temp.copy()


# for k in range(1,301):
# 	print(k)
# 	for i in range(len(grid)-k):
# 		for j in range(len(grid)-k):
# 			a = []
# 			for b in range(k):
# 				a += grid[i+b][j:j+k]
# 			ret = sum(a)
# 			if  ret> res:
# 				res = ret
# 				resInd = (j,i, k)
#print(grid)
print(resInd)