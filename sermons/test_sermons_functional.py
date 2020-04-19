from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import platform


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

    # Select the Add button for Sermons
    driver.find_element_by_css_selector('.model-sermons > td:nth-child(2) > a:nth-child(1)').click()

    title = 'Test Sermon'
    date = '2020-04-19'
    description = 'This is a test sermon.'

    # Populate Title, Date, Description, File
    driver.find_element_by_id('id_title').send_keys(title)
    driver.find_element_by_id('id_date').send_keys(date)
    driver.find_element_by_id('id_description').send_keys(description)


    elem = driver.find_element_by_xpath("//input[@type='file']")
    elem.send_keys("/Users/chaz/music/garageband/rotmk.mp3")

    driver.find_element_by_name("_save").click()

    # Test first sermon at top of list
    added_sermon = driver.find_element_by_css_selector('tr.row1:nth-child(1) > th:nth-child(2) > a:nth-child(1)')
    assert(added_sermon.get_attribute('text') == title)

    # Add tests to verify sermon exists on /sermons page
    # Add tests to verify sermon exists on /sermons{int} detail page

    driver.quit()

    # Test was successful
    if "<selenium.webdriver.firefox.webdriver.WebDriver" in str(driver):
        print("Test for {} was successful".format("Firefox"))
    else:
        print("Test for {} was successful".format("Chrome"))
