
# driver= webdriver.Chrome() #打开浏览器
# driver.maximize_window()#最大化浏览器
 
import sys
sys.path.append("../../../")
from selenium import webdriver
import unittest,time
import HTMLTestRunner #引入HTMLTestRunner 包
from common.sentEmail import sent
import os
import io
import logging
from os import path
#from os import path

class login(unittest.TestCase):
    def _init_(self,verbosity=1):
        self.outputBuffer = io.StringIO()
        self.test_start_time = round(time.time(), 2)
    
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://tsw.xlbzone.com/#/login"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        

    #百度搜索用例

    def test_bd_search(self):
        #登录
        driver = self.driver
        driver.find_elements_by_class_name("ivu-input")[0].send_keys("17620810622")
        driver.find_elements_by_class_name("ivu-input")[1].send_keys("123456")
        driver.find_element_by_class_name("ivu-btn-primary").click()
    def test_bd_search2(self):
        #待施工工单施工
        driver = self.driver
        driver.find_elements_by_class_name("icon-gongdanguanli")[0].click()
        driver.find_elements_by_class_name("ivu-btn-warning")[0].click()
        driver.find_elements_by_class_name("ivu-btn-large")[3].click()
        #self.driver.quit()
    def test_bd_search3(self):
        #待结算工单结算
        driver = self.driver
        time.sleep(1)
        driver.find_elements_by_class_name("ivu-btn-warning")[0].click()
        driver.find_elements_by_class_name("ivu-checkbox-group-item")[2].click()
        driver.find_element_by_class_name("ivu-checkbox-wrapper ivu-checkbox-default").click()
        driver.find_elements_by_class_name("ivu-btn ivu-btn-error").click()
        # price=driver.find_elements_by_class_name("price")[0].text
        # logging.info(price)
        # driver.find_elements_by_class_name("ivu-input-default")[1].send_keys(price)
        # time.sleep(1)
        # driver.find_elements_by_class_name("ivu-btn-error")[0].click()
    # def test_bd_search4(self):
    #     #待出厂工单出厂
    #     driver = self.driver
    #     time.sleep(1)
    #     print ("这是用例4啊")
    #     driver.find_elements_by_class_name("ivu-btn-warning")[0].click()
    #     driver.find_elements_by_class_name("ivu-btn-large")[9].click()

    # def test_bd_search5(self):
    #     #查看完成的工单
    #     driver = self.driver
    #     time.sleep(1)
    #     driver.find_elements_by_class_name("ivu-btn-warning")[1].click()
        
    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":

#测试套件
    suit = unittest.TestSuite()

#添加测试用例到测试套件中
    suit.addTest(login('test_bd_search'))
    # suit.addTest(login('test_bd_search2'))
    # suit.addTest(login('test_bd_search3'))
    # suit.addTest(login('test_bd_search4'))
    #suit.addTest(login('test_bd_search5'))
#报告描述
    title="修连邦登录测试"
    reportTime=time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
    print("报告时间",reportTime)
    reportsName=reportTime + ".html"
    d = path.dirname(__file__)
    reportPath=os.path.abspath('../../..')

#定义个报告存放路径
    filename = reportPath + '/reports/' + reportsName
    fp = open(filename,'wb')

    print("报告输出啊")

#定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=title,
                                           description = u'用例执行情况:')
#运行测试用例
    runner.run(suit)
#关闭报告文件
    fp.close()

#发送邮件
sentreport="reports/" +  reportsName
data=sent(title=title,text=reportTime,touser=['954087620@qq.com'],reports=sentreport)