from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventorioPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        
    def obtener_productos(self):
        return self.driver.find_elements(By.CLASS_NAME,"inventory_item")
    
    def obtener_nombre_primer_producto(self):
        producto = self.obtener_productos()
        
        return producto[0].find_element(By.CLASS_NAME,"inventory_item_name").text
        #lo mismo con precio
        
    def obtener_precios(self):
        return self.driver.find_elements(By.CLASS_NAME,"inventory_item")
      
    def obtener_precio_primer_producto(self):
        precio =self.obtener_precios()
        
        return precio[0].find_element(By.CLASS_NAME,"inventory_item_price").text
    
    def menu_visibule(self):
        menu = self.driver.find_element(By.ID,"react-burger-menu-btn")
        
        return menu.is_displayed()
    
    def filtro_visible(self):
        filtro = self.driver.find_element(By.CLASS_NAME,"product_sort_container")
        
        return filtro.is_displayed()
    
    def agregar_producto(self,nombre):
         productos = self.obtener_productos()
         for producto in productos:
             nombre_producto = producto.find_element(By.CLASS_NAME,"inventory_item_name").text
             if nombre_producto == nombre:
                 producto.find_element(By.TAG_NAME,"button").click()
                 return
             
         raise AssertionError(f"Producto no encontrado:{nombre}")      
     
    def buscar_carrito(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))).text
    
    def ingresar_carrito(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link"))).click()