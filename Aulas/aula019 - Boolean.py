print(10 > 9)
print(10 < 9)
print(10 == 9)

a = 200
b = 33

if b > a:
    print("Sim, b é maior que a")
else:
    print("Não, b não é maior que a")
    
print(bool("Ola"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))
x = 0
y = ""
print(bool(x))
print(bool(y))

#valores que retornan false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def myFuction():
    return True

print(myFuction())

if myFuction():
    print("Sim")
else:
    print("Não")
    
x = 200
print(isinstance(x, float))