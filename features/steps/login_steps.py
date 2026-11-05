from behave import given,when,then
from pages.login_page import LoginPage

@given("que el usuario se encuentre en la pagina del login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir_pagina()
    
    
@when('ingresa en los campos de datos "{standard_user}" y "{secret_sauce}"')
def step_ingresar_credenciales(context,usuario,contraseña):
    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_contraseña("contraseña")
    
@when("hace click en el boton de login")    
def step_login_click(context):
    context.login_page.login_click()
    
@then("deberia ingresar al inventario")   
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url
    