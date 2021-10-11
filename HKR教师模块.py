from selenium import webdriver
import time
driver = webdriver.Chrome()
#登录汉科软
driver.get("http://localhost:8080/HKR")
driver.maximize_window()
#教师登录
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
#输入账号
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
#输入密码
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
#点击登录
driver.find_element_by_xpath("//*[@id='submit']").click()

# a)教师管理：查询，重置密码
#点击教师管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_11']/span[4]/a").click()
# 点击窗口标题教师管理
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[1]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("曹士明")
#点击查询
driver.find_element_by_xpath("//*[@id='search_user']/span").click()
time.sleep(2)
#点击重置密码
driver.find_element_by_xpath("//*[@id='main_panel']/div/div/div[2]/div[2]/div[2]").click()
driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[9]/div/a").click()
time.sleep(1)
driver.switch_to.alert.accept()

# b)学生管理：姓名和电话号码查询、设置毕业和未毕业状态
#点击学生管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_12']/span[4]/a").click()
#点击窗口学生管理
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[3]/a[1]/span[1]").click()
driver.find_element_by_xpath("//*[@id='J-stu']").send_keys("123")
driver.find_element_by_xpath("//*[@id='J-phone']").send_keys("15824700635")
#设置毕业未毕业
#点击查询
driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[2]").click()
time.sleep(1)
#点击设为毕业
driver.find_element_by_xpath("//*[@id='datagrid-row-r2-2-0']/td[11]/div/a").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[9]/div[3]/a").click()  # 点击确定

# c)课程管理：添加、取消添加课程
# 点击课程管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_13']/span[4]/a").click()
# 点击窗口课程管理
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[4]/a[1]/span[1]").click()
time.sleep(1)
#点击添加课程
driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span/span[1]").click()
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").send_keys("java3")
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").send_keys("0基础入门课程")
time.sleep(2)
#点击添加
driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[1]/span").click()
#点击确定
driver.find_element_by_xpath("/html/body/div[12]/div[3]/a/span/span").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[2]/span").click()#取消
#点击添加课程
driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span/span[1]").click()
time.sleep(2)
#点击取消
driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[2]/span").click()
time.sleep(1)

# d)评价：查询评价，导出当前评价、评价报表
driver.find_element_by_xpath("//*[@id='_easyui_tree_15']/span[4]/a").click()
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[5]/a[1]/span[1]").click()
driver.find_element_by_xpath("//*[@id='J-xl']").click()
#点击今日
driver.find_element_by_xpath("//*[@id='laydate_today']").click()
#点击查询
driver.find_element_by_xpath("//*[@id='eva']/div/div/div[1]/table/tbody/tr/td[2]/a/span").click()
time.sleep(1)
#该日无评价 点击确定
# driver.find_element_by_xpath("/html/body/div[13]/div[3]/a/span").click()
#点击导出当前评价
driver.find_element_by_xpath("//*[@id='eva']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()
time.sleep(1)
#点击确定
# driver.find_element_by_xpath("/html/body/div[13]/div[3]/a/span/span").click()
#评价报表
driver.find_element_by_xpath("//*[@id='_easyui_tree_16']/span[4]/a").click()
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[6]/a[1]/span[1]").click()
time.sleep(1)
# e)历史操作日志：日期查询日志，导出当前操作历史
driver.find_element_by_xpath("//*[@id='_easyui_tree_18']/span[4]/a").click()
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[7]/a[1]/span[1]").click()
time.sleep(1)
# i.分页显示数据量，第xx页模块
driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[10]/a/span/span[2]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[10]/a/span/span[2]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[10]/a/span/span[2]").click()
time.sleep(2)
# driver.quit()
