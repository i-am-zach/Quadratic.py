from polynomial import Quadratic

a = int(input('Enter squared coefficient: '))
b = int(input('Enter linear coefficient: '))
c = int(input('Enter constant coefficient: '))

quad = Quadratic(a, b, c)
print(quad)
print(quad.factor_str())