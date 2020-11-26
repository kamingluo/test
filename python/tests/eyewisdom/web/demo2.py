
#coding:utf8
from selenium import webdriver  # webdriver属于selenium的API
import unittest  # unittest是python自带的模块
import time
class test_mail_login(unittest.TestCase):  # 定义一个类并集成 unittest 基类中的 TestCase 类
    def setUp(self):   # 每个测试case运行之前运行（前置条件）
        self.driver = webdriver.Chrome()  # 驱动谷歌浏览器
        self.driver.get("https://www.baidu.com")  # 获取百度URL
        self.driver.set_window_size(800, 1000)  # 窗口大小设置
        # self.driver.maximize_window()  # 窗口最大化
        time.sleep(2)
        self.driver.find_element_by_id("kw").send_keys("网易")  # 百度输入框定位并键入关键字
        time.sleep(3)
        self.driver.find_element_by_id("su").click()  # 点击搜索按钮
        self.driver.implicitly_wait(5)  # 页面静置5秒，无任何动作
    def test_mail_loginsuc(self):  # 设计测试用例（case）重点注意，方法名必须以【test_】开头
        self.driver.find_element_by_id("op_email3_username").send_keys("testerhunter")
        time.sleep(2)
        self.driver.find_element_by_class_name("op_email3_password").send_keys("123456hunter")
        time.sleep(2)
        self.driver.find_element_by_class_name("c-btn").click()
        self.handles = self.driver.window_handles  # 获取所有句柄
        self.driver.switch_to_window(self.handles[-1])  # 句柄转换，获得当前句柄
        time.sleep(3)
        txt = self.driver.find_element_by_id("spnUid").text  # 获取页面固定内容的文本
        print(txt)
        self.assertEqual(txt, "testerhunter@163.com")  # 做断言处理，判断实际结果与期望结果是否一致
    def tearDown(self):  # 每个测试case运行完之后执行（后置条件）
        self.driver.delete_all_cookies()  # 清空所有cookies值，让页面更清洁，反应更快，避免造成缓存问题
        self.driver.quit()  # 关闭浏览器
 
if __name__ == '__main__':
    unittest.main()  # 这种执行方式，用例的执行顺序是无序的