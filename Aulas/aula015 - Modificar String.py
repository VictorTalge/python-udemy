a = "Victor Talge"
b = a.upper()
print(b)
print(a.lower())

a = "   Victor Talge   "
print(a)
print(">" + a + "<")
print(">" + a.strip() + "<")
b = a.strip()
print(b)

a = "Victor Talge"
print(a.replace("Talge","Maciel"))

a = "Carro,Moto,Caminhão"

print(a.split(","))