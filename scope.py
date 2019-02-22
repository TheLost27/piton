x = 0;
def f():
	return x;
def g():
	x = 2
	return f()
a = g()
print(a)

