def newman_prime(n):
	if n == 0 or n == 1:
		return 1
	a = 1
	b = 1
	c = 1
	for _ in range(2, n + 1):
		c = 2 * b + a
		a = c
		b = b + 1
	return c