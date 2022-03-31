#palindrome string:Method1
def palindrome(str):
	return str == str[::-1]

str="madam"
print(palindrome(str))

#palindrome string:Method2
def palin(str):
	for i in range(0,int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

str="malayalam"
print(palin(str))
print("next check")
"""
malayalam
012345678

range(0,int(9/2))=range(0,4)
str[0]!=str[9-0-1]
str[0]!=str[8]
m!=m
true
"""

##check if string is palindrome
def palindromechk(s):
	start=0
	flag=0
	last=len(s)-1
	mid=(len(s)-1)//2

	while (start <= mid):
		if (s[start] == s[last]):
			start += 1
			last -= 1
		else:
			flag=1
			break;

	if flag == 0:
		print("palindrome")
	else:
		print("not a palindrome")

s="madam"
palindromechk(s)