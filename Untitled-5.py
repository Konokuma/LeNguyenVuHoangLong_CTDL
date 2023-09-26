a = "a string"
b = ["my", "second", "favorite", "list"]
c = (1, 2,3,"tuple")
print(a[3:7])
print(a[1:-2])
print(b[1:])
print(c[:2])
mylist = [1,3,5]
mytuple = (1, 2, 'skip a few', 99, 100)
myset = {'a', 'b', 'z'}
mystring = 'abracadabra'
mydict = {'a': 96, 'b': 97, 'c': 98}
for item in mylist:
    print(item)
for item in mytuple:
    print(item)
for element in myset:
    print(element)
for character in mystring:
    print(character)
for key in mydict:
    print(key)
for key, value in mydict.items():
    print(key, value)
for value in mydict.values():
    print(value)
for i in range(10):
    j = 10 * i + 1
    print(j, end='  ' )

