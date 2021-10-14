from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('C:\\Users\\Gainious\\Dev\\bryanu\\AFS-215\\drivers\\chromedriver.exe')
driver.implicitly_wait(40)
driver.set_page_load_timeout(50)
driver.get("https://google.com")
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("Hello world")
search_bar.send_keys(Keys.RETURN)
driver.close()

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# def setUp(self):
#     driver = webdriver.Chrome('C:\\Users\\Gainious\\Dev\\bryanu\\AFS-215\\drivers\\chromedriver.exe')
#     driver.implicitly_wait(40)
#     driver.set_page_load_timeout(50)
# def test_search(self):
#     self.driver.get("https://google.com")
#     search_bar = self.driver.find_element_by_name("q")
#     search_bar.clear()
#     search_bar.send_keys("Hello world")
# def tearDown(self):
#     self.driver.close()