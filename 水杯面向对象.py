'''
  分析一个水杯的属性和功能，使用类描述并创建对象
'''

class cup:
    height = 0
    volume = 0
    color =""
    material =""

    def into(self):
        print("这是一个高度为：",self.height,"cm，容积为",self.volume,
              "ml,颜色为：",self.color,"材质为：",self.material,"的杯子"
              )
a = cup()

a.height = 20
a.volume = 500
a.color = "蓝色"
a.material="玻璃"
a.into()