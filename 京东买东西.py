from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 事件链

driver = webdriver.Chrome()
#进入京东
driver.get("https://www.jd.com/")
driver.maximize_window()
#搜索thinkpad
driver.find_element_by_xpath("//*[@id='key']").send_keys("thinkpad  e580")
#点击搜索
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
time.sleep(2)
# 点击商品
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]").click()

# 切换窗口
# 获取浏览器所有的窗口句柄
data = driver.window_handles # ["s001","s002"]
# 切换具体窗口
driver.switch_to.window(data[1])

#点击加入购物车
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("19910720313")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("hy622301")
#点击登录
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
# #滑动滑块
ac = ActionChains(driver)
# 获取滑块元素
ele = driver.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
ac.click_and_hold(ele).move_by_offset(198,40).perform() # perform执行
ac.release() # 释放
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(2)
driver.quit()














