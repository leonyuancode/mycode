#Day 9：Python 字符串和正则介绍总结
# 一、基本操作
# 1、反转字符串
s = "python"
re=''.join(reversed(s))
print(re)
re_2=s[::-1]
print(re_2)
# 2、字符串切片
java,python = "java", "python"
jl,pl=len(java),len(python)
print([str(java[i%3*jl:] + python[i%5*pl:] or i) for i in range(1,10)])
# 3、join串联字符串
mystr=['I','love','Python']
res='_'.join(mystr)
print(res)
#4、分割字符串
print(res.split('_'))
#5、替换,字符串替换，使用 replace 方法,原字符串并未改变
print(res.replace("_"," "))#I love Python
print(res)#I_love_Python
#6、子串判断
a='our'
c='bb'
b='flourish'
print(a in b)#True
print(b.find(a))#2
print(b.find(c))#-1
#7、去空格，清洗字符串时，位于字符串开始和结尾的空格，有时需要去掉，strip 方法能实现。原字符串并未改变
a = '  \tI love python  \b\n'
print(a.strip())
print(a)
#8字符串的字节长度,encode 方法对字符串编码后：
def str_byte_len(mystr:str):
    mystr_byte=mystr.encode('utf-8')
    return (len(mystr_byte))

print(str_byte_len('i love you'))


