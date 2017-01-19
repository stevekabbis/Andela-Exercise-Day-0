def find_missing(a,b):
	set_a = set(a)
	set_b = set(b)

	if len(set_a) ==len(set_b):
		return 0

	else:
		c = set_a ^ set_b
		return (list(c)[0])
