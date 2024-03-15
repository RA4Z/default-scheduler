from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SeleniumBrouser:
    def __init__(self):
        self.driver = None

    def close_browser(self):
        if self.driver:
            self.driver.quit()

    def navigate_to_url(self, url:str):
        self.driver = webdriver.Edge()
        self.driver.get(url)

    def write_into_element(self, element_xpath:str, texto:str):
        field = self.driver.find_element(By.XPATH, element_xpath)
        field.clear()
        field.send_keys(texto)

    def click_element(self, element_xpath:str):
        field = self.driver.find_element(By.XPATH, element_xpath)
        field.click()

    def clear_element(self, element_xpath:str):
        field = self.driver.find_element(By.XPATH, element_xpath)
        field.clear()

    def press_enter(self, element_xpath:str):
        self.driver.find_element(By.XPATH, element_xpath).send_keys(Keys.RETURN)

    def wait_time(self, time:int):
        self.driver.implicitly_wait(time)

    def get_element_value(self, element_xpath:str):
        return self.driver.find_element(By.XPATH, element_xpath).get_attribute("innerHTML")

    def await_for_element(self, element_xpath:str, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )