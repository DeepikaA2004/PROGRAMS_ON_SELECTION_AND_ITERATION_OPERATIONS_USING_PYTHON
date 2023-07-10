num = int(input('Enter a number:'))

if num % 2 == 0:
    rev = 0
    temp = num
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if rev == temp:
        print('The given number is a palindrome.')
    else:
        print('The given number is not a palindrome.')
else:
    def factorial(num):
        if num == 1:
            return num
        else:
            return num * factorial(num - 1)
    
    print('The factorial of', num, 'is', factorial(num))
    
    count = 0
    n = factorial(num)
    while n > 0:
        n = n // 10
        count = count + 1
    
    print('The number of digits in the factorial of the number is', count)
