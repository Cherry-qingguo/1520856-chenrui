def reversal(str):
	if str == "":#若为空则直接输出
		return str
	elif(len(str)>=1):#若长度大于0则递归至子字符串
		return reversal(str[1:])+str[0]

str1=input('请输入字符串:')
str2=reversal(str1)
print(str2)