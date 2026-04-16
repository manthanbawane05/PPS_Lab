import fibonacci_module
n = int(input())

if n > 0:
	fib_series = fibonacci_module.generate_fibonacci_sequence(n)
	print(' '.join(map(str, fib_series)))
else:
	print("Please enter a positive integer")

def generate_fibonacci_sequence(max_value):
	if max_value<=0:
		return[]
	seq=[]
	a=0
	b=1
	while a <= max_value:
		seq.append(a)
		a, b=b, a+b
	return seq