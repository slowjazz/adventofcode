inp = """
Step G must be finished before step W can begin.
Step X must be finished before step S can begin.
Step F must be finished before step V can begin.
Step C must be finished before step Y can begin.
Step M must be finished before step J can begin.
Step K must be finished before step Z can begin.
Step U must be finished before step W can begin.
Step I must be finished before step H can begin.
Step W must be finished before step B can begin.
Step A must be finished before step Y can begin.
Step Y must be finished before step D can begin.
Step S must be finished before step Q can begin.
Step N must be finished before step V can begin.
Step H must be finished before step D can begin.
Step D must be finished before step Q can begin.
Step L must be finished before step E can begin.
Step Q must be finished before step E can begin.
Step T must be finished before step R can begin.
Step J must be finished before step P can begin.
Step R must be finished before step E can begin.
Step E must be finished before step V can begin.
Step O must be finished before step P can begin.
Step P must be finished before step B can begin.
Step Z must be finished before step V can begin.
Step B must be finished before step V can begin.
Step Y must be finished before step B can begin.
Step C must be finished before step B can begin.
Step Q must be finished before step T can begin.
Step W must be finished before step P can begin.
Step X must be finished before step Z can begin.
Step L must be finished before step T can begin.
Step G must be finished before step Y can begin.
Step Y must be finished before step R can begin.
Step E must be finished before step B can begin.
Step X must be finished before step E can begin.
Step Y must be finished before step V can begin.
Step H must be finished before step L can begin.
Step L must be finished before step J can begin.
Step S must be finished before step T can begin.
Step F must be finished before step T can begin.
Step Y must be finished before step J can begin.
Step A must be finished before step H can begin.
Step P must be finished before step Z can begin.
Step R must be finished before step O can begin.
Step X must be finished before step F can begin.
Step I must be finished before step O can begin.
Step Y must be finished before step Q can begin.
Step S must be finished before step D can begin.
Step Q must be finished before step B can begin.
Step C must be finished before step D can begin.
Step Y must be finished before step N can begin.
Step O must be finished before step Z can begin.
Step G must be finished before step D can begin.
Step A must be finished before step O can begin.
Step U must be finished before step N can begin.
Step Y must be finished before step P can begin.
Step E must be finished before step O can begin.
Step I must be finished before step Q can begin.
Step W must be finished before step O can begin.
Step D must be finished before step B can begin.
Step Z must be finished before step B can begin.
Step L must be finished before step B can begin.
Step P must be finished before step V can begin.
Step C must be finished before step E can begin.
Step S must be finished before step O can begin.
Step U must be finished before step T can begin.
Step U must be finished before step O can begin.
Step Y must be finished before step L can begin.
Step N must be finished before step L can begin.
Step Q must be finished before step Z can begin.
Step U must be finished before step L can begin.
Step U must be finished before step D can begin.
Step J must be finished before step O can begin.
Step L must be finished before step R can begin.
Step S must be finished before step P can begin.
Step H must be finished before step R can begin.
Step F must be finished before step I can begin.
Step D must be finished before step T can begin.
Step C must be finished before step M can begin.
Step W must be finished before step D can begin.
Step R must be finished before step V can begin.
Step U must be finished before step S can begin.
Step K must be finished before step R can begin.
Step D must be finished before step V can begin.
Step D must be finished before step R can begin.
Step I must be finished before step E can begin.
Step L must be finished before step O can begin.
Step T must be finished before step Z can begin.
Step A must be finished before step E can begin.
Step D must be finished before step Z can begin.
Step H must be finished before step V can begin.
Step A must be finished before step L can begin.
Step W must be finished before step R can begin.
Step F must be finished before step A can begin.
Step Y must be finished before step Z can begin.
Step I must be finished before step P can begin.
Step F must be finished before step J can begin.
Step H must be finished before step B can begin.
Step G must be finished before step Z can begin.
Step C must be finished before step K can begin.
Step D must be finished before step E can begin.
"""

x = inp.splitlines()[1:]

# map steps to parents, keep looping, if no parents, add to list

children = {} #letter: list of children
parents = {} #letter: list of parents (will upate)
tot = set()

for i in x:
	dat = i.split()
	p = dat[1]
	c = dat[-3]
	if p not in children:
		children[p] = [c]
	else:
		children[p].append(c)
	if c not in parents:
		parents[c] = [p]
	else:
		parents[c].append(p)
	if p not in parents:
		parents[p] = []
	if c not in children:
		children[c] = []

	tot.add(p)
	tot.add(c)

q = sorted(list(tot))
time = 0
workQueue = ""
work = {}
worknum = 5
done = set()
offset = 60
done.add("")
print(parents)
def parentsDone(parents):
	d = True
	for p in parents:
		if p not in done:
			d = False
	return d

while q or workQueue:
	
	noAdds = True
	while len(workQueue) <worknum and noAdds:
		for i in q:
			if  parentsDone(parents[i]) and i not in work:
				noAdds = False
				workQueue += i 
				work[i] = 1
				q.remove(i)

		if noAdds:
			noAdds = False

	print(time, workQueue, [work[i] for i in workQueue])
	for i in workQueue:
		work[i] +=1
		if i in work and (work[i]> (offset+ord(i)-ord('A')+1)) :
			done.add(i)
			r = workQueue.index(i)
			workQueue = workQueue[:r] + workQueue[r+1:]

	time +=1

print(time)





