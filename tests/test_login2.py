from pages.login_page import LoginPage
import pytest
from utils.reader import lector_users_csv
from utils.logger import logger

#@pytest.mark.flaky(reruns=2,reruns_delay=5) reruns and delay per test
@pytest.mark.parametrize(
    "data",lector_users_csv())
def test_login(driver,data):
    try:
        
        logger.info("Prueba de login") #tal vez borrar despues ejemplo para logger
        login_page = LoginPage(driver)
    
        driver.get("https://www.saucedemo.com/")
    
        login_page.login(data["usuario"],data["password"])
    
    
        if data["user_type"] == "user_approved":
        
            assert "/inventory.html" in driver.current_url
    
        elif data["user_type"] == "user_fake":
            error = login_page.get_error_message()
            print("\n",error)
            assert "Epic sadface" in error
            logger.info("Prueba de error exitosa")
    except Exception:
        logger.exception("Error durante prueba de login")
        raise