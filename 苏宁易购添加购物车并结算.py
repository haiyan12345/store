from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 事件链

driver = webdriver.Chrome()
#进入京东
driver.get("https://suning.com/")
driver.maximize_window()

#输入口红
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("口红")
#点击搜索
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
#点击商品
driver.find_element_by_xpath("//*[@id='0010329978-12320251361']/div").click()
# 切换窗口
# 获取浏览器所有的窗口句柄
data = driver.window_handles # ["s001","s002"]
# 切换具体窗口
driver.switch_to.window(data[1])
#点击加入购物车
driver.find_element_by_xpath("//*[@id='addCart']").click()
#去购物车结算
driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()
#点击去结算
driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()
time.sleep(2)
driver.quit()