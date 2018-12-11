players = 10
last = 1618
arr = []

players = 435
last = 7118400

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
 
 
class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None
 
    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)
 
    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)
 
    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.first = new_node
 
    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next
 
    def display(self):
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.first:
                break

curMarble = 1
#curptr = 1
time = -1
arr = [0]
scores = {}

l = CircularDoublyLinkedList()
l.insert_at_beg(Node(0))
curptr = l.first
while True:
	#l.display()
	#print("\n")
	if curMarble%10000==0:
		print(curMarble)
	#print(time%(players)+1, arr)
	if curMarble>last:
		break
	if curMarble>1 and curMarble%23==0:
		
		for i in range(7):
			curptr = curptr.prev
		# if curptr <0:
		# 	curptr = len(arr)+ curptr 
		# t = arr[curptr]

		t = curptr.data

		#pop at curptr
		newptr = curptr.next
		l.remove(curptr)
		curptr = newptr

		#arr.pop(curptr)

		p = time%(players)+1
		if p not in scores:
			scores[p] = 0
		scores[p] += (t + curMarble)
		# curptr stays the same
		# if curptr==len(arr)-2:
		# 	curptr = 0


		time +=1
		curMarble +=1
		continue

	else:
		# nextIndex = curptr + 2
		# if nextIndex > len(arr):
		# 	nextIndex = (nextIndex % len(arr)) +1# revisit
		# if curptr == len(arr)-1:
		# 	nextIndex = 1
		
		# arr.insert(nextIndex, curMarble)

		nextIndex = curptr.next
		l.insert_after(nextIndex, Node(curMarble))
		curMarble +=1
		time +=1
		curptr = nextIndex.next
		# if curptr > len(arr):
		# 	curptr = curptr % len(arr) +1# revisit
		continue
	
#print(scores)
res = 0
for k, v in scores.items():
	res = max(res, v)

print(res)


