'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），
行为（打字，打游戏，看视频）
'''

class notebookComputer:
    __username = ""
    __size = 0
    __price = 0
    __CPUtype = ""
    __Memorysize = 0
    __Standbylength =""

    def shownotebookComputer(self):
        print("这是一台屏幕大小为：",self.__size,
              "寸,价格为：",self.__price,
              "元,型号为：",self.__CPUtype,
              "内存大小为：",self.__Memorysize,
              "G，待机时长为：",self.__Standbylength,
              "的联想笔记本电脑"
              )
    def setUsername(self,username):
        self.__username = username
    def setSize(self,size):
        if size < 0:
            print("电脑屏幕大小不能小于0")
        else:
            self.__size = size

    def setPrice(self,price):
        if price < 1000:
            print("电脑价格不能小于等于1000")
        else:
            self.__price = price

    def setCPUtype(self,CPUtype):
        self.__CPUtype = CPUtype

    def setMemorySize(self,Memorysize):
        if Memorysize < 0:
            print("内存大小不能小于0")
        else:
            self.__Memorysize = Memorysize

    def setStandbyLength(self,Standbylength):
        self.__Standbylength = Standbylength

    def write(self,write):
        print(self.__username,"正在用电脑",write)

    def game(self,gamename):
        print(self.__username,"正在用电脑打",gamename)

    def video(self,videoname):
        print(self.__username,"正在用电脑看",videoname,"的视频")


c = notebookComputer()
c.setUsername("杨幂")
c.setSize(15)
c.setPrice(50000)
c.setCPUtype("i710900k")
c.setMemorySize(256)
c.setStandbyLength("2h")

c.shownotebookComputer()
c.write("打字")
c.game("王者荣耀")
c.video("速度与激情")