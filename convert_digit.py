# Converting number in dec to the selected number base

print('Input number in dec')
x = int(input())
print('Input number base')
base = int(input())

y_revers = ''
y = ''

while x > 0:
    y_revers += str(x % base)
    x //= base
  
for i in range(len(y_revers) - 1, -1, -1):
    y += y_revers[i] 
    
print(y, end = '\n')
print(y, end = '')
print(y)