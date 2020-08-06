#二、正则表达式
import  re
"""
首先，认识常用的元字符：
    . 匹配除 "\n" 和 "\r" 之外的任何单个字符。
    ^ 匹配字符串开始位置
    $ 匹配字符串中结束的位置
    * 前面的原子重复 0 次、1 次、多次
    ? 前面的原子重复 0 次或者 1 次
    + 前面的原子重复 1 次或多次
    {n} 前面的原子出现了 n 次
    {n,} 前面的原子至少出现 n 次
    {n,m} 前面的原子出现次数介于 n-m 之间
    ( ) 分组，输出需要的部分
再认识常用的通用字符：
    \s 匹配空白字符
    \w 匹配任意字母/数字/下划线
    \W 和小写 w 相反，匹配任意字母/数字/下划线以外的字符
    \d 匹配十进制数字
    \D 匹配除了十进制数以外的值
    [0-9] 匹配一个 0~9 之间的数字
    [a-z] 匹配小写英文字母
    [A-Z] 匹配大写英文字母
"""
# 1、search 第一个匹配串使用正则模块，search 方法，找出子串第一个匹配位置。
s='i love python very much'
pat='python'
r=re.search(pat,s)
print(r.span())
#2、
"""match 与 search 不同
正则模块中，match、search 方法匹配字符串不同
具体不同：
    match 在原字符串的开始位置匹配
    search 在字符串的任意位置匹配"""
s='flourish'
recom=re.compile('our')
print(recom.match(s))# 返回 None，找不到匹配
res = recom.search(s)
print(res.span())#(2, 5) # OK, 匹配成功，our 在原字符串的起始索引为 2
# 字符串 ourselves，ours 才能 match 到 our。
#3、finditer 匹配迭代器
# 使用正则模块，finditer 方法，返回所有子串匹配位置的迭代器。
#通过返回的对象 re.Match，使用它的方法 span 找出匹配位置。
s = '山东省潍坊市青州第1中学高三1班'
pat='1'
r=re.finditer(pat,s)
for i in r:
    print(i)  #<re.Match object; span=(9, 10), match='1'><re.Match object; span=(14, 15), match='1'>
# 4、findall 所有匹配 ，findall 方法能查找出子串的所有匹配
s = '一共20行代码运行时间13.59s'
# 目标查找出所有所有数字：通用字符 \d 匹配一位数字 [0-9]，+ 表示匹配数字前面的一个字符 1 次或多次。
pat=r'\d+\.?\d*'
r=re.findall(pat,s)
print(r)
s = [-16, 1.5, 11.43, 10, 5]
pat = r'^[1-9]\d*$'
print([i for i in s if re.match(pat,str(i))])
#5、re.I 忽略大小写re.I 是方法的可选参数，表示忽略大小写。
s = 'That'
pat ='t'
r = re.finditer(pat,s,re.I)
for i in r:
    print(i.span())
#6、split 分割单词
s = 'id\tname\taddress'
print(s.split('\t'))
s = 'This,,,   module ; \t   provides|| regular ; '
words = re.split('[,\s;|]+',s)
print(words)
#7、sub 替换匹配串
content="hello 12345, hello 456321"
pat=re.compile(r'\d+') #要替换的部分
m=pat.sub("666",content)
print(m)
#8、compile 预编译如果要用同一匹配模式，做很多次匹配，可以使用 compile 预先编译串。
s = [-16,'good',1.5, 0.2, -0.1, '11.43', 10, '5e10']
rec = re.compile(r'^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$')
print([ i for i in s if rec.match(str(i))])
content = '''
       <h>ddedadsad</h>
       <div>graph</div>
       <div>math</div>'''
result = re.findall(r'<div>(.*?)</div>',content)
print(result)
