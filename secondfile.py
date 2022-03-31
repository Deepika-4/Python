#interchange first and last element in a list
def swap(list):
	size = len(list)

	temp=list[0]
	list[0]=list[size-1]
	list[size-1]=temp

	return list

list = [1,2,3,4,5]
print(swap(list))	


#palindrome string
def palindrome(str):
	return str == str[::-1]

str="madam"
print(palindrome(str))