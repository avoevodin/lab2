# Samples of list compregensions

A = [x ** 2 for x in range(10)] # squares from 0 to 9
print(A)

A = [1, -4, 2, 6, 12, 3, 6, 5, 19, 4]

# creating array of squares of positive even numbers, excluding odd numbers
B = [0 if x < 0 else x ** 2 for x in A if x % 2 == 0] 
                                    
print(B)