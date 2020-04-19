# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
#
# with webdriver.Firefox() as driver:
#
#     wait = WebDriverWait(driver, 10)
#
#     # Navigate to the Contact form
#     driver.get("http://localhost:8000/contact")
#
#     # Enter form information to submit
#     subject = 'Prayer Request'
#     name = 'Chaz'
#     email = 'csselph@gmail.com'
#     message = 'Please Lord, help our friend Brian.'
#
#     driver.find_element_by_name('subject').send_keys(subject)
#     driver.find_element_by_name('name').send_keys(name)
#     driver.find_element_by_name('email').send_keys(email)
#     driver.find_element_by_name('body').send_keys(message)
#     driver.find_element_by_css_selector("button[type='submit']").click()
#     alert_message = driver.find_element_by_xpath("//div[@class='alert alert-primary messages']")
#
#     # Login to Admin Dashboard to delete new submission
#     driver.get("http://localhost:8000/admin")
#     driver.find_element_by_name('username').send_keys('chaz')
#     driver.find_element_by_name('password').send_keys('123god1;')
#     driver.find_element_by_css_selector("input[type='submit']").click()
#
#     # Navigate to the Contacts section of Admin Dashboard
#     driver.find_element_by_link_text('Contacts').click()
#     driver.find_element_by_xpath("//tr[@class='row1']/td[@class='action-checkbox']/input[@name='_selected_action']").click()
#     driver.find_element_by_xpath("//div[@class='actions']/label/select[@name='action']").click()
#     driver.find_element_by_xpath("//div[@class='actions']/label/select[@name='action']/option[@value='delete_selected']").click()
#     driver.find_element_by_xpath("//div[@class='actions']/button[@type='submit']").click()
#
#     # Delete the new submission
#     driver.find_element_by_xpath("//input[@type='submit']").click()
#
#     # Assert the submission was deleted
#     driver.find_element_by_xpath("//ul[@class='messagelist']/li[@class='success']")
#     time.sleep(3)
#
#     print("Test succeeded")
#     driver.quit()
