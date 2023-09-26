infinity_plus_one = float('inf') + 1
print("infinity_plus_one has type", type(infinity_plus_one))
s = "Hello, "
t = "World."
u = s + t
print(type(u))
print(u)
print(u[9])
n = str(9876)
print(n[2])
L = [1,2,3,4,5,6]
print(type(L))
L.append(100)
print("The first item is", L[0])
print("The second item is", L[1])
print("The last item is", L[-1])
print("The second to last item is", L[-2])
t = (1, 2, "skip a few", 99, 100)
print(type(t))
print(t)
print(t[4])
d = dict()
d[5] = "five"
d[2] = "two"
d['pi'] = 3.1415926
print(d)
print(d['pi'])
s = {2,1}
print(type(s))
s.add(3)
s.add(2)
s.add(2)
s.add(2)
print(s)






