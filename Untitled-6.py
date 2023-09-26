if 3 + 3 < 7:
    print("This should be printed.")
if 2 ** 8 != 256:
    print("This should not be printed.")
if False:
    print("This is bad.")
else:
    print("This will print.")
x = 1
while x < 128:
    print(x, end=' ')
    x = x * 2
y = "not a number"
try:
    f = float(y)
except ValueError:
    print("\nYou can't do that!")
def foo(c, d):
    return 8 * c + d
print(foo(2, 1))
print(foo("Na", " batman"))
def foo(e):
    return e + 2
def bar(somefunction):
    return somefunction(4)
print(bar(foo))
somevariable = foo
print(bar(somevariable))



