from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from day01.day03自动化框架.InitPage import InitPage
from day01.day03自动化框架.LoginOperation import LoginOpera
import time

@ddt
class TestLogin(TestCase):
    # 在所有方法执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(r"http://localhost:8080/HKR")
        time.sleep(1)
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()  # 退出浏览器


    @data(*InitPage.data)
    def testSuccessCase1(self,testdata):

        # 提取数据
        username = testdata["username"]
        time.sleep(1)
        password = testdata["password"]
        expect = testdata["expect"]

        # 调用被测操作类
        loginObj = LoginOpera(self.driver)
        time.sleep(2)
        loginObj.login(username,password)

        # 获取实际结果
        da = loginObj.getSuccessResult()
        #  断言
        self.assertEqual(da,expect)


    @data(*InitPage.data1)
    def testSuccessCase2(self,testdata):

        # 提取数据
        username = testdata["username"]
        password =  testdata["password"]
        expect =  testdata["expect"]

        # 调用被测操作类
        loginObj = LoginOpera(self.driver)
        time.sleep(2)
        loginObj.login(username,password)

        # 获取实际结果
        da = loginObj.getErrorResult()

        #  断言
        self.assertEqual(da,expect)






















