
# multi lines string in single variable
var='''Hello
My name is Ravi and i Live in Patna'''

print(var)

#capitalizing the letters
var = 'learning python is fun '
res1=var.capitalize()
print(res1)


# printing some text at centre
var1 = "python"
res2=var1.center(20,"-")
print(res2)

# find()
s1 = 'I love my India '
print(s1.find("India"))  # Lower index first occurance of india

#format
s1="I got {n:2f} points in mathe "
print(s1.format(n=69))

#Index
s2='python is an interesting language'
print(s2.index('python'))

# Is alpha numeric
s3='mh101'
print(s3.isalnum())

s4='Data Science'
print(s4.isalnum())

#is digit
s1='800002'
print(s1.isdigit())

#is lower

s6='python'
print(s6.islower())

s7='Python'
print(s7.istitle())

# Splitting the functions
name ='Ravi Ranjan kumar'
first_Name, middle_Name, last_Name = name.split(' ')
print(first_Name)
print(middle_Name)
print(last_Name)