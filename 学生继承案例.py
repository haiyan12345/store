'''
i.人：年龄，性别，姓名
ii.现在有个工种，工人：年龄，性别，姓名 。
行为：干活。请用继承的角度来实现该类。
iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。
行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
'''

class people:
     age = 0
     sex = ""
     name = ""

     def setAge(self,age):
          self.age = age
     def setSex(self,sex):
          self.sex = sex
     def setName(self,name):
          self.name = name
     def show(self):
          print(self.age,"的",self.sex,"生",self.name)


class worker(people):
      work = ""

      def setWork(self,work):
           self.work = work
      def show(self):
           print(self.age,"的",self.sex,"生",self.name,"正在",self.work)

c = worker()
c.name = "晓彤"
c.sex = "女"
c.age= 18
c.work = "工作"
c.show()

class student(people):
     id = ""
     def setId(self,id):
          self.id = id
     def sing(self):
          print("学号为",self.id,"的",self.name,"正在唱歌")
     def study(self):
          print("学号为",self.id,"的",self.name,"正在学习")

xs = student()
xs.id = 1002
xs.name ="迪丽热巴"
xs.sing()
xs.id = 1005
xs.name = "杨幂"
xs.study()