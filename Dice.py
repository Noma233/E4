import random 

print('What is your name?')
print('>', end="")
name = input()
print('Hello,', name, '!!')

print('Rolling the dice...')

x1 = random.randrange(5) + 1
x2 = random.randrange(5) + 1

print("Die 1: ", x1)
print("Die 2: ", x2)

print("Total value: ", x1 + x2)

if x1 + x2 > 7:
	print(name, 'won!!')
else:
	print(name, 'lost.')
