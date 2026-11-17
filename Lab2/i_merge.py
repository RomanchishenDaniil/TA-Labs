def merge_sort_iterative(a):
	n = len(a)
	comparisons = 0
	assignments = 0
	i = 1
	print(f"Початковий масив: {a}\n")
	
	while i < n:
		j = 0
		while j < n - i:
			left = j
			mid = j + i
			right = min(j + 2 * i, n)
			print(f"Об'єднуємо підмасиви: a[{left}:{mid}] ({a[left:mid]}) і a[{mid}:{right}] ({a[mid:right]})")
			c, a_count = merge_iter(a, left, mid, right)
			comparisons += c
			assignments += a_count
			print(f"Масив після об'єднання: {a}\n")
			j += 2 * i
		i *= 2
	return a, comparisons, assignments

def merge_iter(a, left, mid, right):
	comparisons = 0
	assignments = 0
	n1 = mid - left
	n2 = right - mid
	
	L = a[left:mid]
	R = a[mid:right]
	assignments += n1 + n2
	
	it1 = 0
	it2 = 0
	k = left
	assignments += 3
	
	while it1 < n1 and it2 < n2:
		comparisons += 1
		print(f"  Порівняння: {L[it1]} < {R[it2]} -> {L[it1] < R[it2]}")
		if L[it1] < R[it2]:
			a[k] = L[it1]
			it1 += 1
			assignments += 1
		else:
			a[k] = R[it2]
			it2 += 1
			assignments += 1
		k += 1
		assignments += 1
		
	while it1 < n1:
		a[k] = L[it1]
		it1 += 1
		k += 1
		assignments += 1
		
	while it2 < n2:
		a[k] = R[it2]
		it2 += 1
		k += 1
		assignments += 1
		
	return comparisons, assignments

my_list = [90, 10, 15, 80, 100, 6, 57, 5, 29]
sorted_list, comps, assigs = merge_sort_iterative(my_list.copy())
print("Фінальний відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоювань: {assigs}")
