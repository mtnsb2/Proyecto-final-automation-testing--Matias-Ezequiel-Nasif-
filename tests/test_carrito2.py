from pages.login_page import LoginPage
from pages.inventorio_page import InventorioPage
from pages.carrito_page import CarritoPage

from utils.reader import read_products_json

def test_carrito(driver):
    login_page=LoginPage(driver)
    inventario_page=InventorioPage(driver)
    carrito_page = CarritoPage(driver)
    
    driver.get("https://www.saucedemo.com/")
    
    login_page.login("standard_user","secret_sauce")
    
    producto = read_products_json()[0]
    
    inventario_page.agregar_producto(producto["nombre"])
    
    assert inventario_page.buscar_carrito() == "1"
    
    inventario_page.ingresar_carrito()
    
    assert carrito_page.verificar_producto() == producto["nombre"]
    
    assert carrito_page.verificar_precio() == producto["precio"]
    