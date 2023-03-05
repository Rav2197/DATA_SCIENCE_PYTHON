name = input("Please enter your name \n")
print("My name is ",name)

# by default it takes input as string

num1 = int(input("Please Enter 1st number\n"))
num2 = int(input("Please Enter 2nd number\n"))
sum = num1+num2
print("The sum is ",sum)


num3,num4,num5 = map(int,input("please enter three numbers").split())
sum = num3+num4+num5
print('The sum is ',sum)

name1, name2 = input("please enter the name").split()
print("first_name : "+name1)
print("last name : "+name2)


name = input("Please enter your name ")
print(f'hello {name} ! good morning')


# String Formatting

x = 5
y =10

print('the value of x is {} and value of y is {}'.format(x,y))

# order of python format argument

print('Python programming is used in {0} and {1}'.format('Datascience','web dev'))