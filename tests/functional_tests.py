from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


with webdriver.Firefox() as driver:

    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost:8000/contact")

    navbar = driver.find_element_by_class_name('navbar')

    subject = driver.find_element_by_name('subject')
    name = driver.find_element_by_name('name')
    email = driver.find_element_by_name('email')
    message = driver.find_element_by_name('body')
    submit_button = driver.find_element_by_id('submit')

    subject.send_keys('Prayer Request')
    time.sleep(1)

    name.send_keys('Chaz')
    time.sleep(1)

    email.send_keys('csselph@gmail.com')
    time.sleep(1)

    message.send_keys('Please Lord, help our friend Brian during this trying time.')
    time.sleep(1)

    submit_button.click()

    time.sleep(5)

    alert_message = driver.find_element_by_xpath("//div[@class='alert alert-primary messages']")

    time.sleep(2)
    print("Test succeeded")
    driver.quit()
