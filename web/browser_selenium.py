from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SeleniumBrouser:
    def __init__(self):
        self.driver = webdriver.Edge()

    def close_browser(self):
        if self.driver:
            self.driver.quit()

    def navigate_to_url(self, url:str):
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

if __name__ == "__main__":
    web_nav = SeleniumBrouser()
    
    web_nav.navigate_to_url('https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada#google_vignette')
    state_id = '//*[@id="__nuxt"]/div/div[2]/section/div[3]/div[2]/div/div/div/div/div[1]/input'
    city_id = '//*[@id="__nuxt"]/div/div[2]/section/div[3]/div[3]/div/div/div/div/div[1]/input'

    web_nav.write_into_element(state_id,'Santa Catarina')
    web_nav.wait_time(10)
    web_nav.click_element('/html/body/div[2]/div/div[2]/section/div[3]/div[2]/div/div/div/div/div[2]/div')

    web_nav.write_into_element(city_id,'Schroeder')
    web_nav.wait_time(10)
    web_nav.click_element('/html/body/div[2]/div/div[2]/section/div[3]/div[3]/div/div/div/div/div[2]/div')

    web_nav.press_enter(city_id)

    web_nav.wait_time(10)
    web_nav.await_for_element('/html/body/div[2]/div/div[2]/section/div[6]/div/div/a[1]')
    web_nav.click_element('/html/body/div[2]/div/div[2]/section/div[6]/div/div/a[1]')

    web_nav.await_for_element('//*[@id="__nuxt"]/div/div[2]/section/div[8]/div/nav/ul/li[4]/a')
    total = int(web_nav.get_element_value('//*[@id="__nuxt"]/div/div[2]/section/div[8]/div/nav/ul/li[4]/a'))
    
    for i in range(total):
        web_nav.wait_time(10)
        for target in range(20):
            cnpj_id = f'//*[@id="__nuxt"]/div/div[2]/section/div[9]/div[1]/div/div/div/div/div[{target+1}]/article/div/div/p/strong[1]'
            web_nav.await_for_element(cnpj_id)
            print(web_nav.get_element_value(cnpj_id))

        web_nav.wait_time(10)
        web_nav.await_for_element('/html/body/div[2]/div/div[2]/section/div[8]/div/nav/a[2]')
        web_nav.click_element('/html/body/div[2]/div/div[2]/section/div[8]/div/nav/a[2]')

    #web_nav.close_browser()