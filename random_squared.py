import random

num1 = random.randint(1,15)
num2 = random.randint(1,15)
answer = num1 * num1 - num2
print(num1 , '*' ,num1, '-', num2 , '= ?')
guess = int(input('Answer:'))

if guess == answer:
  print('''Well done, you got it right!
__/\__
\    /
 |/\|''')
else:
  print('Na, na na naa, na, na. It is', answer)
