from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


with webdriver.Firefox() as driver:

    wait = WebDriverWait(driver, 10)


    driver.set_window_size(1024, 768)


    driver.get("http://localhost:8000/contact")

    navbar = driver.find_element_by_class_name('navbar')

    subject = 'Prayer Request'
    name = 'Chaz'
    email = 'csselph@gmail.com'
    message = 'Please Lord, help our friend Brian.'


    driver.find_element_by_name('subject').send_keys(subject)
    time.sleep(1)
    driver.find_element_by_name('name').send_keys(name)
    time.sleep(1)
    driver.find_element_by_name('email').send_keys(email)
    time.sleep(1)
    driver.find_element_by_name('body').send_keys(message)
    time.sleep(1)

    driver.find_element_by_css_selector("button[type='submit']").click()

    time.sleep(5)

    alert_message = driver.find_element_by_xpath("//div[@class='alert alert-primary messages']")

    time.sleep(2)



    # Go to Admin Dashboard to delete new post

    driver.get("http://localhost:8000/admin")

    time.sleep(2)

    driver.find_element_by_name('username').send_keys('chaz')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('123god1;')
    time.sleep(1)

    driver.find_element_by_css_selector("input[type='submit']").click()

    time.sleep(2)

    driver.find_element_by_link_text('Contacts').click()

    time.sleep(2)

    driver.find_element_by_xpath("//tr[@class='row1']/td[@class='action-checkbox']/input[@name='_selected_action']").click()


    # driver.find_element_by_xpath("div[@class='actions']/label/select[@name='action']").click()


    print("Test succeeded")
    driver.quit()
