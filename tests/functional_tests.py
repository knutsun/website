from selenium import webdriver

browser = webdriver.Firefox()

# User opens website
browser.get('http://localhost:8000')

# User reads Gateway Baptist Church in the web page title
assert 'Gateway Baptist Church' in browser.title

browser.quit()
