from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        
    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")    
            
    def ingresar_usuario(self,usuario):
        self.driver.find_element(By.ID,"user-name").send_keys(usuario)
        
    def ingresar_contraseña(self,contraseña):
        self.driver.find_element(By.ID,"password").send_keys(contraseña)
        
    def login_click(self):
        self.driver.find_element(By.ID,"login-button").click()

    def get_error_message(self):
        error_text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error > h3")))
        return error_text.text
        
    def login(self,usuario,contraseña):
        self.ingresar_usuario(usuario)    
        self.ingresar_contraseña(contraseña)
        self.login_click()    
        
                
        
