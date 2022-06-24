import 邮箱模板
from search import *
from mylac import *
from 分析 import *
from 邮箱模板 import *

def inputbaseinfo():
       名称 = input("请输入目标名称： ")
       a = "可选择的切入话题："
       print(a)
       mylist = search(名称)
       text1 = mylac(mylist)
       f = open("text.txt","w")
       f.write(a+text1)
       f.close()

if __name__ == '__main__':
       inputbaseinfo()
       年龄 = int(input("请输入人物年龄： "))
       if 年龄 < 22:
              text2 = 学生方案()
              f = open("text.txt","a")
              f.write(text2)
              f.close()
              print(text2)

       elif 22 <= 年龄 <= 30:
              text2 = 非学生方案()
              f = open("text.txt", "a")
              f.write(text2)
              f.close()
              print(text2)
       elif 30 <= 年龄 <= 50:
              text2 = 中年方案()
              f = open("text.txt", "a")
              f.write(text2)
              f.close()
              print(text2)
       else:
              text2 = 老年方案()
              f = open("text.txt", "a")
              f.write(text2)
              f.close()
              print(text2)

       youxiangtitle = "\n"+"常见的邮箱话题话术： \n"
       f = open("text.txt", "a")
       f.write(youxiangtitle)
       f.close()
       if 年龄 < 22:
              text2 = 邮箱模板.学生邮件话题["热点事件"]+邮箱模板.学生邮件话题["节假日相关"]+邮箱模板.学生邮件话题["身份属性"]
              f = open("text.txt","a")
              f.write(text2)
              f.close()
              print(text2)

       elif 22 <= 年龄 <= 30:
              text2 = 邮箱模板.非学生邮件话题["工作人员"]["关系属性"]+邮箱模板.非学生邮件话题["工作人员"]["环境属性"]+邮箱模板.非学生邮件话题["工作人员"]["身份属性"]+邮箱模板.非学生邮件话题["工作人员"]["计算机相关"]+邮箱模板.非学生邮件话题["非工作人员"]["环境属性相关"]+邮箱模板.非学生邮件话题["非工作人员"]["社会利益相关"]
              f = open("text.txt", "a")
              f.write(text2)
              f.close()
              print(text2)
       elif 30 <= 年龄 <= 50:
              text2 = 邮箱模板.非学生邮件话题["工作人员"]["关系属性"]+邮箱模板.非学生邮件话题["工作人员"]["环境属性"]+邮箱模板.非学生邮件话题["工作人员"]["身份属性"]+邮箱模板.非学生邮件话题["工作人员"]["计算机相关"]+邮箱模板.非学生邮件话题["非工作人员"]["环境属性相关"]+邮箱模板.非学生邮件话题["非工作人员"]["社会利益相关"]
              f = open("text.txt", "a")
              f.write(text2)
              f.close()
              print(text2)
       else:
              text2 = 邮箱模板.非学生邮件话题["工作人员"]["关系属性"]+邮箱模板.非学生邮件话题["工作人员"]["环境属性"]+邮箱模板.非学生邮件话题["工作人员"]["身份属性"]+邮箱模板.非学生邮件话题["工作人员"]["计算机相关"]+邮箱模板.非学生邮件话题["非工作人员"]["环境属性相关"]+邮箱模板.非学生邮件话题["非工作人员"]["社会利益相关"]
              f = open("text.txt", "a")
              f.write(text2)
              f.close()
              print(text2)

