from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class LandingPage(BasePage) :
    def __init__(self, driver: webdriver, waitTime: float) -> None:
        super().__init__(driver,waitTime)

    @property
    def page_header(self) -> WebElement:
        return self._driver.find_element(
            by=By.XPATH, value="//h1[.='FINDING THE TRUTH' and not(@style)]")
    
    @property
    def start_button(self)-> WebElement:
        return self._wait.until(
            EC.visibility_of_element_located((By.XPATH,'//*[.="START"]/ancestor::a')))
    @property
    def learning_score(self)-> WebElement:
        return self._wait.until(
            EC.visibility_of_element_located((By.XPATH,'//*[contains(text(),"Your score so far")]'))
        )

    def get_project_link(self, learning_name: str) -> WebElement:
        return self._wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,f'//*[.="{learning_name}"]/ancestor::a' )))