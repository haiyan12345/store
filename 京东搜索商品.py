from selenium import webdriver
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开百度网址
chromeDriver.get("http://www.JD.com")

# 窗口最大化
chromeDriver.maximize_window()

#寻找搜索输入框
chromeDriver.find_element_by_xpath("//*[@id = 'key']").send_keys("电脑")

# 点击搜索按钮
chromeDriver.find_element_by_xpath("//*[@class= 'button']").click()
time.sleep(1)
chromeDriver.find_element_by_xpath("//*[@class = 'gl-i-wrap']").click()
chromeDriver.get("https://item.jd.com/100014047052.html")
time.sleep(1)
# 退出浏览器
# chromeDriver.quit()