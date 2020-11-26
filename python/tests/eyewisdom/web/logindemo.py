
#coding:utf8
import sys
sys.path.append("../../")
import HTMLTestRunner #引入HTMLTestRunner 包
from common.sentEmail import sent
import os
from os import path
from selenium import webdriver  # webdriver属于selenium的API
import unittest  # unittest是python自带的模块
import time



class test_login(unittest.TestCase):  # 定义一个类并集成 unittest 基类中的 TestCase 类
    def setUp(self):   # 每个测试case运行之前运行（前置条件）
        self.driver = webdriver.Chrome()  # 驱动谷歌浏览器
        self.driver.get("https://t-eyewisdom.vistel.cn/login")  # 获取百度URL
        self.driver.set_window_size(800, 1000)  # 窗口大小设置
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(5)  # 页面静置5秒，无任何动作
    def test_loginsuc(self):  # 设计测试用例（case）重点注意，方法名必须以【test_】开头
        self.driver.find_element_by_id("username").send_keys("luojiaming")
        self.driver.find_element_by_id("password").send_keys("a3216953")
        time.sleep(1)
        self.driver.find_element_by_class_name("login-btn").click()
        time.sleep(5)
        # self.handles = self.driver.window_handles  # 获取所有句柄
        # self.driver.switch_to_window(self.handles[-1])  # 句柄转换，获得当前句柄
        # time.sleep(3)
        # txt = self.driver.find_element_by_id("spnUid").text  # 获取页面固定内容的文本
        # print(txt)
        # self.assertEqual(txt, "testerhunter@163.com")  # 做断言处理，判断实际结果与期望结果是否一致

    # def test_newpatient(self):
        self.driver.find_elements_by_class_name("el-menu-item")[1].click()#点击患者列表
        self.driver.find_elements_by_class_name("button-primary")[2].click()#点击新建患者按钮
        time.sleep(10)
        self.driver.find_element_by_id("name").send_keys("kaming0001")
        self.driver.find_element_by_id("age").send_keys("10")
        time.sleep(5)



    def tearDown(self):  # 每个测试case运行完之后执行（后置条件）
        self.driver.delete_all_cookies()  # 清空所有cookies值，让页面更清洁，反应更快，避免造成缓存问题
        self.driver.quit()  # 关闭浏览器
 
if __name__ == '__main__':
    #unittest.main()  # 这种执行方式，用例的执行顺序是无序的
    #测试套件
    suite = unittest.TestSuite()

    #添加测试用例到测试套件中
    suite.addTest(test_login('test_loginsuc'))
    # suite.addTest(test_login('test_newpatient'))

    #报告描述
    title="自定义测试报告啊"
    reportTime=time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
    reportsName=reportTime + ".html"
    d = path.dirname(__file__)
    reportPath=os.path.abspath('../..')

    #定义个报告存放路径
    filename = reportPath + '/reports/' + reportsName
    fp = open(filename,'wb')

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=title,
                                           description = u'用例执行情况:')
    #运行测试用例
    runner.run(suite)
    #关闭报告文件
    fp.close()

    #发送邮件
    # sentreport="reports/" +  reportsName
    # data=sent(title=title,text=reportTime,touser=['954087620@qq.com'],reports=sentreport)