import time
#导入驱动器
from selenium import webdriver

driver = webdriver.Chrome()
#打开文件
driver.get(r"E:\ptyhon自动化测试\软件\10.6的资料\练习的html\跳转页面\pop.html")
#放大页面
driver.maximize_window()

#定位输入框
driver.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(1)
# 关闭浏览器
driver.quit()