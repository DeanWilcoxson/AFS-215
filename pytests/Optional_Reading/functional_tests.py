from selenium import webdriver
# browser = webdriver.Firefox()
browser = webdriver.Chrome()
browser.binary_location = "C:\\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browser.get('http://localhost:8000')
assert 'Django' in browser.title
