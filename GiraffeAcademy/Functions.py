def say_hi(name):
    print("Hello " + name)

user_name = input("Enter your name: ")

say_hi(user_name)

def cube(num):
   return num*num*num

string_number = input("Enter a Number :")
int_number = int(string_number)
result = cube(int_number)
print(result)

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3

print(max_num(1,2,3))


