num1 = int(input("Enter the First Number"))
num2 = int(input("Enter the 2nd Number"))
num3 = int(input("Enter the 3rd Number"))

# Initiallly Largest = nnum1
largest = num1
if num2>largest:
    largest =num2
if num3>largest:
    largest=num3

print(f"the largest number is {largest}")
