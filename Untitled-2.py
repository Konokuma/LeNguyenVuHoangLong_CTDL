x = 5
y = 3.2
z = True
print("x has type", type(x))
print("y has type", type(y))
print("z has type", type(z))
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is c)
print(a == c)
d = 2
print("d =", d)
print("float(d) =", float(d))
print("d still has type", type(d))
print("Overwriting d.")
d = float(d)
print("Now, d has type", type(d))
numstring = "3.1415926"
e = float(numstring)
print("e has type", type(e))
best_number = 73
f = str(best_number)
print("f has type", type(f))
thisworks = float("inf")

