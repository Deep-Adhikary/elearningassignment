
import sys
import os

from behave import fixture, use_fixture

sys.path.append(os.path.abspath('./'))

from utils.webdriver_builder.driver_builder import DriverBuilder
from utils.enums import Browsers
from utils.types import WebDriver
from utils.screenshot import Screenshot

from selenium.webdriver.support.ui import WebDriverWait

@fixture
def selenium_browser(context):
    driver = DriverBuilder().build_for(Browsers.CHROME).set_implicit_wait(5).build()
    driver.implicitly_wait(5)
    driver.maximize_window()
    context.driver=driver
    yield context.driver
    context.driver.quit()

@fixture 
def page_url(context):
    context.page_url='https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a'
@fixture
def explicit_wait_time(context):
    context.explicit_wait_time=10
@fixture
def screenshot(context):
    context.screenshot=Screenshot( context.driver, '../../reports/screenshots')

def before_scenario(context,scenario):
    use_fixture(selenium_browser, context)
    use_fixture(screenshot, context)
    use_fixture(page_url,context)
    use_fixture(explicit_wait_time,context)

def after_step(context, step):
    if step.status == "failed":
        context.screenshot.capture()