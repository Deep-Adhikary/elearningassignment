import os
import allure
from datetime import datetime


from utils.types import WebDriver


class Screenshot:
    def __init__(self,driver:WebDriver,path:str,file_name_format='') -> None:
        self._driver = driver
        self._path = os.path.abspath(path)
        self._file_name_format = file_name_format if file_name_format!='' else '%Y_%m_%d_%H_%M_%S'

    def capture(self) -> None:
        screenshot_file_path=f'{self._path}/{datetime.now().strftime(self._file_name_format)}'
        print(screenshot_file_path)
        self._driver.save_screenshot(f'{screenshot_file_path}.png')
        allure.attach.file(f'{screenshot_file_path}.png',name=screenshot_file_path,attachment_type=allure.attachment_type.PNG)

    