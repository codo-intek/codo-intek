import math
def pytago(a,b):
	result =  float(a*a + b*b)
	return math.sqrt(result)

a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
print(pytago(a,b))