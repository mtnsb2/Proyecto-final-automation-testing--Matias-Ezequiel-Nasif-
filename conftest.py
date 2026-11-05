import pytest
from selenium import webdriver

import pytest_html 
import base64 
import pathlib

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("-private")
    driver = webdriver.Firefox(options=options)
    
    driver.implicitly_wait(5)
    
    yield driver
    
    driver.quit()
    
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return { "x-api-key": "pub_726187485afa204b113fb01fe7deff0fb9aa6abc67c17700d9a86727c58ae792" }

    
@pytest.hookimpl(hookwrapper=True)    
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        
        folder = pathlib.Path("screenshots")
        folder.mkdir(parents=True,exist_ok=True)
        file = folder / f"{item.name}.png"
        
        driver.save_screenshot(str(file))
        
        imagen = base64.b64encode(file.read_bytes()).decode("utf-8")
        report.extras = [
            pytest_html.extra.png(imagen, name="Screenshot")
        ]
