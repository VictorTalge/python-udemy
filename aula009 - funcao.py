
x = "incrivel"
#função é def
def myFunc():
    print("Python é incrivel")
    print("Python é " + x)

myFunc()

print("Você é " + x)

print("===================")

def myFunc1():
    y = "fantastico"
    #como definir dentro de uma função uma variavel global, primeiro você tem que criar ela
    global w 
    w = "10"
    print("Python é " + y)
    print("Python é " + w)

myFunc1()

#irá dar erro, pois y é uma váriavel local, não global
#print("Você é " + y)

print("Você é " + w)

print("===================")

z = "inacreditavel"

print("Você é " + z)

def myFunc2():
    z = "espetacular"
    print("Você é " + z)
    
myFunc2()

print("Você é " + z)