# Using Modulus

print("The quick brown %s jumped upon the lazy dog."%'fox')

x="India"
print('%s is my country and I love my %s'%(x,'country'))

# % used to inject Strings

print("Hello my name is %s"%'Ravi')

# %d is used for injecting integers

print('There are %d states and %d union territories in India '%(29,7))

# Floating point number
print('Floating point number : %1.0f' %(13.1339))



# Formatting String using format() method

print('We all are {} before the law'.format('equal'))

# we can insert objects by using index based position

print('{2} {1} {0}'.format('direction','the','read'))

# Objects can be inserted using assigned keywords

print('a:{a}, b:{b}, c:{c}'.format(a = 1,b= 'Two',c=12.3))


# Formatted Screen

name = 'ELE'

print(f"My name is {name}")

a=10
b=2

print(f"he said his age is {(a*b)+7}")

num = 3.1215978
print(f"the value of pi is : {num:{1}.{5}}")