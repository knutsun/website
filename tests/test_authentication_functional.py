import os
import platform
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


base_path = "http://localhost:8000"
operating_system = platform.system()

if operating_system == 'Darwin' or 'Linux':
    executable_path = "{}/developer/gateway/website/tests/chromedriver".format(os.getenv('HOME'))
else:
    executable_path = "E:\\gwayweb\\website\\tests\\chromedriver"

drivers = [
    webdriver.Chrome(executable_path=executable_path),
    webdriver.Firefox()
]

for driver in drivers:

    wait = WebDriverWait(driver, 10)
    driver.get(base_path)

    # Login to Admin Dashboard
    driver.get("{}/admin".format(base_path))
    driver.find_element_by_name('username').send_keys('chaz')
    driver.find_element_by_name('password').send_keys('123god1;')
    driver.find_element_by_css_selector("input[type='submit']").click()

    # Logout of Admin Dashboard from the Admin Dashboard
    driver.find_element_by_link_text('LOG OUT').click()
    time.sleep(2)
    driver.get("{}/admin".format(base_path))

    # Assert user redirects to login form
    time.sleep(2)
    assert driver.current_url == '{}/admin/login/?next=/admin/'.format(base_path)

    # Login to Admin Dashboard
    driver.get("{}/admin".format(base_path))
    driver.find_element_by_name('username').send_keys('chaz')
    driver.find_element_by_name('password').send_keys('123god1;')
    driver.find_element_by_css_selector("input[type='submit']").click()

    # Assert user is authenticated on Home page navbar
    driver.get(base_path)
    user = driver.find_element_by_xpath("/html/body/header[1]/nav/div/ul[2]/li/a")
    assert user.text == 'chaz'

    # Logout from the Home page navbar
    user.click()
    driver.find_element_by_link_text('Log out').click()

    # Assert user redirects to login form
    driver.get("{}/admin".format(base_path))
    assert driver.current_url == '{}/admin/login/?next=/admin/'.format(base_path)

    driver.quit()

    # Test was successful
    if "<selenium.webdriver.firefox.webdriver.WebDriver" in str(driver):
        print("Test for {} was successful".format("Firefox"))
    else:
        print("Test for {} was successful".format("Chrome"))
