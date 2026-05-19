""""
n = int(input("请输入数字："))
for i in range(n):
    print("*"*i)         *三角      字符串的乘法是n个字符串相乘相当于平方与数字不同
"""
from Lib.importlib.resources import contents

"""
n = int(input())
for i in range(n):
    print(" "* (n-i)+"*"* (2*i-1))    等腰三角 n-i确保*位于中心一次减少空格以致实现等腰 2*i-1保持奇数维持等腰
"""

"""
#两数之和
nums = list(map(int, input("数组(以空格分隔):").split( )))
print(nums)
target = int(input("请输入要查询的数字(以空格分隔):"))
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])
            print("nums[%d]+nums[%d]==%d"%(i,j,target))
while nums[i] + nums[j] != target:
    print("没有两数之和，请重新输入")
    break
"""

"""
列表倒序转为字符串之后字符串拼接再转为整数相加求和再倒序变为新列表

l1 = list(map(int,input("请输入数字(以空格分隔)：").split( )))
l2 = list(map(int,input("请输入数字(以空格分隔)：").split( )))
print(l1,l2)
s1 = int(''.join(map(str,l1[ : :-1])))
s2 = int(''.join(map(str,l2[ : :-1])))
num1 = s1+s2
num2 = list(map(int,(str(num1)[::-1])))
print(num2)
print(f"{s1}+{s2}={num1}")
"""


"""
判断素数
b = int(input("请输入整数："))
def fun_a(x):
    if x <2:
        isPrime = 0
        return isPrime
    if x == 2:
         return 1
    while  x > 2:
         if x % 2 == 0:
             return 0
         elif x % 3 == 0:
             return 0
         else :
             return 1

isPrime = fun_a(b) #通过输入数进行运行函数然后得到isPrime=1 or =0再判断
if isPrime == 1:
    print("是素数")
else:
    print("不是素数")
"""
"""
是素数就加入列表
def fun_b(x,y):
    list =[]
    for i in range(x,y+1):
        def fun_a(x):
            if x < 2:
                return 0
            if x == 2:
                return 1
            while x > 2:
                if x % 2 == 0:
                    return 0
                elif x % 3 == 0:
                    return 0
                else:
                    return 1
        isPrime = fun_a(i)
        if isPrime == 1:
             list.append(i)
    return list
list1 = []
m = int(input("输入第一个数："))
n = int(input("输入第二个数："))
list1 = fun_b(m,n)
print(list1)
"""


#异常专题练习：
#1.
"""
a = input("请输入分数： ") #——input内容都为字符串
def fun_score(score):
    try:
        score = int(a) #——只有数字字符串才能由int转为整型     try-except语法格式3
        if score<10 or score>100:
          raise Exception("分数输出有误")
        if not isinstance(score,(int,float)):
          raise Exception("请输入正确数值")
        print(f"分数合法,为{a}分")
    except:
        print("请输入有效数值")
fun_score(a)
"""

#2.
"""
def check_username(name):
    if len(name)<3:
        raise Exception("用户名长度不得小于3")
    for i in name:
        if i == "@" or "#" or "$":
            raise ValueError("用户不能含特殊符号")
    print(f"用户名格式正确，名字{a}")
a = input("请输入名字：")
check_username(a)
"""

#3.
"""
a = input("请输入数：")
def positive_num(n):
    try:
        b = float(n)
        if not isinstance(b,(int,float)):
              raise TypeError("不是>=0的数")
        if b<0:
              raise ValueError("不是正数")
        print("是合法正数")
    except:
        print("请输入数字")     ————这里没有进行分支异常类型的捕获，所以最后只要输入不符合要求都只会返回请输入数字
positive_num(a)
"""

#4.自定义异常练习
"""
class ScoreError(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return self.message
def funa(score):
    try:
        if score<0 or score>100:
            raise ScoreError("成绩输入必须在0-100")
        print(f"成绩录入正确,录入成绩为{score}")
    except ScoreError as e:               ————这里是对ScorError异常的捕获 输出为错误：成绩输入必须在0-100
        print("错误：",e)
a = int(input("请输入成绩："))
funa(a)


class PwdLengthError(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return self.message
def pwd_length(password):
   try:
       if len(password) == 0:          #len():只能用在字符串，列表，元组，字典
           raise ValueError("密码为空")
       if len(password)<6:
           raise PwdLengthError("密码位数小于6")           不用except 单独抛出就是PwdLengthReeo错误类型
       print(f"您已成功创建密码，密码为{password}")           
   except PwdLengthError as e:
       print("错误：",e)
   except ValueError as e:
       print(e)

a = input("请输入密码:")
print(a)
pwd_length(a)
"""



"""
文件管理练习
with open("my_file.txt",'w+',encoding="utf-8") as L:
    L.write("Python文件管理\n")
    L.write("with上下文管理器\n")
    L.write("自动关闭文件\n")
    L.seek(0)
    print(L.read())

Python文件管理
with上下文管理器
自动关闭文件

with open("my_file.txt",'r',encoding="utf-8") as L:
     content=L.readlines()
     print(content)
     for i in content:
         print(i)
with open("my_file.txt",'a+',encoding="utf-8") as L:
    L.write("追加的第一行\n")
    L.write("追加的第二行\n")
    L.seek(0)
    print(L.read())


try:
    a = input("请输入文件名:")
    with open(a,'r',encoding="utf-8") as L:  #a已经是字符串了，所以不用加引号
        content=L.read()
        print(content)
except FileNotFoundError:
    print("文件不存在")
except Exception as e:
    print("读取文件出错")


students = ["张三,18,男\n",
    "李四,19,女\n",
    "王五,20,男\n",
    "赵六,17,男\n"
            ]
with open("student.txt",'w+',encoding="utf-8") as f:
        f.writelines(students)
        f.seek(0)
        contents = f.readlines()
        print(contents)
        for i in contents:
            print(i.strip().split(","))
            mz,nl,xb=i.strip().split(",")
            print(f"姓名：{mz}，年龄：{nl}")
"""




