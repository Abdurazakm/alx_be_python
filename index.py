# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"name is {self.name} and age is {self.age}")
# student1  = student("John", 20)
# student1.display()
num1 = int(input("Eneter the first number: "))
num2 = int(input("Eneter the second number: "))
try:
    result = num1/num2
    if result < 0:
        raise ValueError("Result is negative, which is not allowed.")
        raise ValueError("Result is negative, which is not allowed.")
    print(f"The result of {num1} divided by {num2} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division was successful.")
finally:
    print("Execution completed.")
        