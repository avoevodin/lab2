# Converting number in dec to the selected number base

import string

alph = string.ascii_lowercase
print(alph)

print('Input number in dec')
x = int(input())

i = 0
base = 0
while i < 3 and (base == 0 or base > 26):
    print('Input number base, is less than 26 required')
    base = int(input())

y_revers = ''
y = ''

while x > 0:
    rem = x % base
    if rem > 9:
        rem = alph[rem - 9]
    else:
        rem = str(rem)
    
    y_revers += rem
    x //= base
  
for i in range(len(y_revers) - 1, -1, -1):
    y += y_revers[i] 
    
# print(y, end = '\n') # shifting down after end of printing
# print(y, end = '') # doing nothing after end of printing
print(y)