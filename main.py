def factor(number):
    return set(thing for thing in range(1, number+1) if number%thing==0)

number1 = factor(int(input('Enter the first number:')))
number2 = factor(int(input('Enter the second number:')))

print(max(number1.intersection(number2)))
