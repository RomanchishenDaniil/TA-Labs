def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

def sink(arr, i, n, counters):
	k = i
	while True:
		j = 2 * k + 1
		if j >= n:
			break
		counters['comparisons'] += 1
		if j + 1 < n and arr[j + 1] > arr[j]:
			j += 1
		counters['comparisons'] += 1
		if arr[k] >= arr[j]:
			break
		swap(arr, k, j)
		counters['assignments'] += 3
		k = j

def heapsort(arr):
	n = len(arr)
	counters = {'comparisons': 0, 'assignments': 0}
	for i in range(n // 2 - 1, -1, -1):
		sink(arr, i, n, counters)
	for i in range(n - 1, 0, -1):
		swap(arr, 0, i)
		counters['assignments'] += 3
		sink(arr, 0, i, counters)
	return arr, counters

arr = [90, 10, 15, 80, 100, 6, 57, 5, 29]
sorted_arr, counts = heapsort(arr.copy())
print(f"Відсортований масив: {sorted_arr}")
print(f"Порівняння: {counts['comparisons']}, Присвоювання: {counts['assignments']}")
