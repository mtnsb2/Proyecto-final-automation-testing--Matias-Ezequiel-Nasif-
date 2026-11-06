from pages.login_page import LoginPage
from pages.inventorio_page import InventorioPage
from utils.logger import logger
import pytest


@pytest.mark.order(2)
def test_inventory(driver):
    try:
        logger.info("Inicio pruebas de inventorio y menus")
        login_page=LoginPage(driver)
        inventario_page=InventorioPage(driver)
    
        logger.info("Ingreso a URL")
        driver.get("https://www.saucedemo.com/")
       
        logger.info("Ingreso de credenciales")
        login_page.login("standard_user","secret_sauce")
        
        logger.info("Prueba de cantidad de productos") 
        productos = inventario_page.obtener_productos()
        
        assert len(productos) == 6 
        logger.info("Cantidad de productos correcta")
        
        logger.info("Pruebas de nombres y precios de productos")
        assert inventario_page.obtener_nombre_productos_index(0)== "Sauce Labs Backpack"
        logger.info("Nombre de primer producto correcto")
        assert inventario_page.obtener_precio_productos_index(0)== "$29.99"
        logger.info("Precio de primer producto correcto")
        assert inventario_page.obtener_nombre_productos_index(1)== "Sauce Labs Bike Light"
        logger.info("Nombre de segundo producto correcto")
        assert inventario_page.obtener_precio_productos_index(1)== "$9.99"
        logger.info("Precio de segundo producto correcto")
        
        logger.info("Pruebas de interaccion con sitio")
        assert inventario_page.menu_visible()
        logger.info("Prueba de interaccion con menu exitosa")
        assert inventario_page.filtro_visible()
        logger.info("Prueba de interaccion con filtro extitosa")
                       
    except Exception:
            logger.exception("Error durante prueba de inventorio")
            raise
    