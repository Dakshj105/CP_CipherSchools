def heapify(li, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and li[largest] < li[l]:
		largest = l

	if r < n and li[largest] < li[r]:
		largest = r

	if largest != i:
		li[i], li[largest] = li[largest], li[i]
		heapify(li, n, largest)

def heapSort(li):
	n = len(li)
	for i in range(n//2 - 1, -1, -1):
		heapify(li, n, i)
	for i in range(n-1, 0, -1):
		li[i], li[0] = li[0], li[i]
		heapify(li, i, 0)

li = list(map(int, input().split()))
heapSort(li)
for i in range(len(li)):
	print(li[i], end = " ")
