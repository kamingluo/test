from selenium import webdriver

from time import sleep
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
driver = webdriver.Chrome()
# browser = webdriver.Firefox(executable_path ="F:\GeckoDriver\geckodriver")

#2.通过浏览器向服务器发送URL请求
driver.get("https://www.baidu.com/")

sleep(3)

#3.刷新浏览器
driver.refresh()

#4.设置浏览器的大小
driver.set_window_size(1400,800)

#5.设置链接内容
element=driver.find_element_by_link_text("新闻")
element.click()

element=driver.find_element_by_link_text("“下团组”时间")
element.click()
