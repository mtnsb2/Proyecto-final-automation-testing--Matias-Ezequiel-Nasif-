import pytest
from pages.login_page import LoginPage
from pages.inventorio_page import InventorioPage
from pages.carrito_page import CarritoPage
from utils.logger import logger

from utils.reader import read_products_json


@pytest.mark.order(3)
def test_carrito(driver):
    try:
        logger.info("Inicio funcionalidad de carrito")
        login_page=LoginPage(driver)
        inventario_page=InventorioPage(driver)
        carrito_page = CarritoPage(driver)
        
        logger.info("Ingreso URL")
        driver.get("https://www.saucedemo.com/")
        
        logger.info("Ingreso de credenciales")
        login_page.login("standard_user","secret_sauce")
        
        logger.info("Pruebas de interaccion con carrito")
        producto = read_products_json()[0]
        
        inventario_page.agregar_producto(producto["nombre"])
        
        assert inventario_page.buscar_carrito() == "1"
        logger.info("Prueba de agregar productos exitosa")
        
        inventario_page.ingresar_carrito()
        
        assert carrito_page.verificar_producto() == producto["nombre"]
        logger.info("Nombre de producto agregado verificado correctamente")
        
        assert carrito_page.verificar_precio() == producto["precio"]
        logger.info("Precio de producto agregado verificado correctamente")
    except Exception:
            logger.exception("Error durante prueba de carrito")
            raise
        
    