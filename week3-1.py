print('Numbers from 1 to 10')

num = 5

x = int(input('Guess the number: '))

while x != num :
    x = int(input('Guess the number: '))
    if x == num :
        break
print('Great! You did it!')
