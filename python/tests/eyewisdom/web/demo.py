
# driver= webdriver.Chrome() #打开浏览器
# driver.maximize_window()#最大化浏览器
 
import sys
sys.path.append("../../")
from selenium import webdriver
import unittest,time
import HTMLTestRunner #引入HTMLTestRunner 包
from common.sentEmail import sent
import os
from os import path
#from os import path

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"


    #百度搜索用例

    def test_bd_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()

    def test_bd_search2(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw2").send_keys("kaming")#故意写错，产生错误用例
        driver.find_element_by_id("su").click()


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":

#测试套件
    print("1111111")
    suit = unittest.TestSuite()

#添加测试用例到测试套件中
    print("2222222")
    suit.addTest(Baidu('test_bd_search'))
    suit.addTest(Baidu('test_bd_search2'))

#报告描述
    print("333333")
    title="自定义测试报告啊"
    reportTime=time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
    reportsName=reportTime + ".html"
    d = path.dirname(__file__)
    reportPath=os.path.abspath('../..')

#定义个报告存放路径
    print("44444")
    filename = reportPath + '/reports/' + reportsName
    fp = open(filename,'wb')

#定义测试报告
    print("55555555")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=title,
                                           description = u'用例执行情况:')
#运行测试用例
    print("6666666")
    runner.run(suit)
#关闭报告文件
    fp.close()

#发送邮件
sentreport="reports/" +  reportsName
data=sent(title=title,text=reportTime,touser=['954087620@qq.com'],reports=sentreport)