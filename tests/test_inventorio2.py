from pages.login_page import LoginPage
from pages.inventorio_page import InventorioPage


def test_inventory(driver):
    login_page=LoginPage(driver)
    inventario_page=InventorioPage(driver)
    
    driver.get("https://www.saucedemo.com/")
    
    login_page.login("standard_user","secret_sauce")
    
    productos = inventario_page.obtener_productos()
    
    assert len(productos) == 6 
    
    assert inventario_page.obtener_nombre_primer_producto()== "Sauce Labs Backpack"
    assert inventario_page.obtener_precio_primer_producto()== "$29.99"
    
    assert inventario_page.menu_visibule()
    assert inventario_page.filtro_visible()
    
    
    