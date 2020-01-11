# 定义一 变量
#变量的赋值
name = 'Tom'
a = 0
print(name,a)

name1=name2=name3="lucy"
print(name1,name2,name3)

one,two,three = 1,2,3
print(one,two,three)
# number1,number2,number3=4 这种情况会报错

#ps：py的基本语言包括字符串（string），数字（numeric），列表（list），元组（tumple），字典（dictionary）


# 定义二  字符串(String)
name1 = 'Tom'
name2 = "Tom"   # 用单引号，双引号乃至三引号进行定义的变量

# 定义三 切片   格式：String[左下表：右下标]
hallo = "welcome to this world"
print(hallo[0:15])  
print(hallo[:])
print(hallo[:18])
print(hallo[0:])  
print(hallo[:])   # 和上面的效果是一样的

# 其他常用操作
# 1.
print(len(hallo)) # 获取字符串的长度
# 2.
print('C:\back\name') # \b \n是转义字符，不能按原样显示
print(R'C:\back\name')  # 用r或者R放在前面就按原样显示了
# 3.
print('cat'*2) # 将cat重复输出两次
# 格式字符串%
age = 10
print("Tom's name is %d"%(age))












      
