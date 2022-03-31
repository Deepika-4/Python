#printing statement
print('Hello world')

#sum of two numbers: Method 1
num1 = 2
num2 = 7

sum = num1 + num2

print("sum of two numbers {0} and {1} is {2}" .format(num1,num2,sum))

#sum of two numbers: Method2
num3=input("enter first number:")
num4=input("enter second number:")

#user might enter float values
sum = float(num3) + float(num4)

print("sum of two input numbers {0} and {1} is {2}" .format(num3,num4,sum))

#max of two numbers: MEthod1
def max(a,b):
	if a >= b:
		return "Max of {0} and {1} is {0}" .format(a,b)
	else:
		return "Max of {0} and {1} is {1}" .format(a,b)

print(max(3,4))

#max of two numbers: Method2: using math function
a=3
b=9

print(max(a,b))

#max of two numbers: Method3: using ternary operator
a = 2
b = 4
 
# Use of ternary operator
print(a if a >= b else b)

#find simple interest
def simpleint(p,r,t):
	si = (p * r * t)/100
	#print('The Simple Interest is', si)
	return "simple interest is : {3}".format(p,r,t,si)

print(simpleint(8,6,8))

#find compund interest
def compint(p,r,t):
	amt = p * pow((1 + r/100),t)
	ci = amt - p
	return "Compound interest is : {4}".format(p,r,t,amt,ci)

print(compint(10000,10.25,5))

#find area of circle
def area(r):
	area= 3.14 * r * r
	return "area of circle is {1} ".format(r,area)
print(area(2))