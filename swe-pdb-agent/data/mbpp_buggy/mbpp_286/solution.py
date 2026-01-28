def max_sub_array_sum_repeated(a, n, k): 
	modifed = a * k
	current = 0
	max_sum = modifed[0]
	for num in modifed:
		current += num
		if current < 0:
			current = 0
		if current > max_sum:
			max_sum = current
	return max_sum