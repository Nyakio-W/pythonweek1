#variables
site_name = 'powerlearnproject'
site_name = '2.3'
print(site_name)
print(site_name)

a,b,c = 1, 2, 'hello'
print(a)
print(b,c)

site1 = site2 ='PLP'
print(site1)
print(site2)

#data types

num = 24 #here we just understand that it is an integer type - we don't have to define it in python

num1=5 
print(num1 ,'is of type', type(num1))
num2 =2.0
print(num2 ,'is of type', type(num2))
num3= 1+2j
print(num3 ,'is of type', type(num3))

languages =['swift','java','python']
print(languages)
print(languages[0])
print(languages[2])

product = ('microsoft','Xbox','499.99')
print(product[0])
print(product[2], type(product))

languages[1] = 'php'
print(languages)

name = 'python'
print(name)
message = 'python for beginners'
print(message)

student_id = {112,113,114,120}
print(student_id)
print(type(student_id))

capital_city = {'nepal':'kathmandu','italy':'rome','england':'london'}
print(capital_city['nepal'])
print(capital_city['italy'])

#type conversion, comments, indentation
integer_number = 123
float_number = 1.23
new_number = integer_number + (float_number)
print(new_number)
print('data type', type(new_number)) #here it has converted 123 to a loat 123.00 so that it can be added

new_number = integer_number + int(float_number)
print(new_number)
print('data type', type(new_number)) #here we forced 1.13 to be an int 1 so when we added it was 124

num_string ='12'
num_integer = 23

print('data type of num_string before type casting',type(num_string))

num_string = int(num_string) #the word 'int' here has forced it to be an integer so that we can add it

print('data type of num_string after type casting',type(num_string))

num_sum = num_integer + num_string
print("sum:",num_sum)
print('data type of num_sum', type(num_sum))

"""
is this a comment? - it isss
yasss
"""

#basic operations
a = 10
b = 5
a+=b #a=a+b
print(a)

a=5
b=6
print((a>2)) and (b>=6) #true - and, or , not


x = 'hello world'
print('h' in x) #membership opertors, will test whether that value/variable is present - true or false

#printing output and collecting user input in Python
x= 'hello world'
print(x)

x = raw_input('tell me your name:')
# x = str(raw_input('tell me your name:')) #casting

print(x)