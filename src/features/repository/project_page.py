from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class ProjectPage(BasePage) :
    def __init__(self, driver: webdriver, waitTime: float) -> None:
        super().__init__(driver,waitTime)

    @property
    def project_title(self) -> WebElement:
        return self._driver.find_element(
            by=By.XPATH, value='')

    def get_project_header(self, header_text: str) -> WebElement:
        return self._wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f'//*[contains(text(),"{header_text}")]')))

    @property
    def get_judge_button(self)-> WebElement:
        return self._wait.until(
            EC.visibility_of_element_located((By.XPATH,'//*[.="JUDGE THIS"]/ancestor::a')))
    
    def get_answer_radio_button(self,text)->WebElement:
        return self._wait.until(
            EC.visibility_of_element_located((By.XPATH,f'//*[.="{text}"]/parent::span')))

    @property
    def vote_button(self):
        return self._wait.until(
            EC.visibility_of_element_located((By.XPATH,'//*[.="VOTE"]/ancestor::a'))
        )
    
    def get_response_header_text(self,text):
        return self._wait.until(
            EC.visibility_of_element_located((By.XPATH,f'//*[.="{text}"]/ancestor::h2'))
        )