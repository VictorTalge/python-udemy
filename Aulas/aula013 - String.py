a = "Victor"
b = "Seja bem vindo"
c = '''Lorem Ipsum Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... 
Lorem Ipsum Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...'''
d = """Lorem Ipsum Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... 
Lorem Ipsum Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."""

print(d)

e = "Ola Mundo!"

print(e)

print(e[1])

for x in "Victor": 
    print(x)
   
y = len(e)
print(y)

txt = "Seja bem vindo ao curso de Python."
x = "vindo" in txt
print(x)
print("carro" in txt)

if x == True:
    print("Correto")
else:
    print("Incorreto")
    
if "lucas" in txt:
    print("vindo está presente")
else:
    print("Não há está palavra")
    
if x: 
    print("vindo está presente")
    
if "vindo" in txt: 
    print("vindo está presente")

if "vindo" not in txt: 
    print("vindo não está presente") 