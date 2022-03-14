import math as m

n = int(input("Enter an Integer: "))
print(n)

f = 1/m.sqrt(5)*(((1+m.sqrt(5))/2)**n-((1-m.sqrt(5))/2)**n)

print(m.floor(f))

# first 12 Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# 
# solve for n Choose 2

print(m.comb(n, 2))





