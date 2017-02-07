from selenium.webdriver.common.by import By


def login(driver, username="admin", password="Password"):
    # driver.find_element_by_id("txtUsername").clear()
    #  driver.find_element_by_id("txtUsername").send_keys(username)
    type(driver, By.ID, "txtUsername", username)
    type(driver, By.ID, "txtPassword", password)
    # driver.find_element_by_id("txtPassword").clear()
    # driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

def logout(driver):
    driver.find_element_by_id("welcome").click()
    driver.find_element_by_link_text("Logout").click()

def type(driver, by, selector, text):
    element = driver.find_element(by, selector)
    element.clear()
    element.send_keys(text)
