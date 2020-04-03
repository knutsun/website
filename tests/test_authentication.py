from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Firefox() as driver:

    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost:8000/")

    # Login to Admin Dashboard
    driver.get("http://localhost:8000/admin")
    driver.find_element_by_name('username').send_keys('chaz')
    driver.find_element_by_name('password').send_keys('123god1;')
    driver.find_element_by_css_selector("input[type='submit']").click()

    # Logout of Admin Dashboard from the Admin Dashboard
    driver.find_element_by_link_text('LOG OUT').click()
    driver.get("http://localhost:8000/admin")

    # Assert user redirects to login form
    assert driver.current_url == 'http://localhost:8000/admin/login/?next=/admin/'

    # Login to Admin Dashboard
    driver.get("http://localhost:8000/admin")
    driver.find_element_by_name('username').send_keys('chaz')
    driver.find_element_by_name('password').send_keys('123god1;')
    driver.find_element_by_css_selector("input[type='submit']").click()

    # Assert user is authenticated on Home page navbar
    driver.get("http://localhost:8000/")
    user = driver.find_element_by_xpath("/html/body/header[1]/nav/div/ul[2]/li/a")
    assert user.text == 'chaz'

    # Logout from the Home page navbar
    user.click()
    driver.find_element_by_link_text('Log out').click()

    # Assert user redirects to login form
    driver.get("http://localhost:8000/admin")
    assert driver.current_url == 'http://localhost:8000/admin/login/?next=/admin/'

    print("Test successful")
