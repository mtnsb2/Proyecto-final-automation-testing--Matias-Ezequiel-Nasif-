from pages.login_page import LoginPage
import pytest
from utils.reader import lector_users_csv
from utils.logger import logger

#@pytest.mark.flaky(reruns=2,reruns_delay=5) reruns and delay per test (ejemplo en caso de aplicar por prueba)

@pytest.fixture(scope="module",autouse=True)
def log_inicio_api():    
    logger.info("Inicio pruebas de login")
    yield 

@pytest.mark.order(1)
@pytest.mark.parametrize(
    "data",lector_users_csv())
def test_login(driver,data):
    try:
             
        login_page = LoginPage(driver)

        logger.info("Ingreso URL")
        driver.get("https://www.saucedemo.com/")
    
        logger.info("Ingreso de credenciales")
        login_page.login(data["usuario"],data["password"])
    
        if data["user_type"] == "user_approved":
        
            assert "/inventorys.html" in driver.current_url
            logger.info("Prueba de login exitosa")
        
            
        elif data["user_type"] == "user_fake":
            error = login_page.get_error_message()
            print("\n",error)
            assert "Epic ssadface" in error
            logger.info("Prueba de mensaje de error exitosa")
            
            
    except Exception:
        logger.exception("Error durante prueba de login")
        raise
    