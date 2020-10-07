def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

number1 = 50
number2 = 50

print("\n")
result = multiplication_or_sum(num1, num2)
print("The result is", result)