number = float(input("provide your Desired Marks "))
if number >=90:
    grade="A+"
elif number >=80:
    grade="A"
elif number >=70:
    grade="B"
else:
    grade="Fail"

print(f"The grade is {grade}")