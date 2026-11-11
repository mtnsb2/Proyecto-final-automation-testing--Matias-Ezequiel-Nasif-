from behave import given,when,then
from pages.login_page import LoginPage

@given("que el usuario se encuentre en la pagina del login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir_pagina()
    
    
@when('ingresa en los campos de datos "{usuario}" y "{password}"')
def step_ingresar_credenciales(context,usuario,password):
    if usuario == "VACIO":
        usuario = ""
        
    if password == "VACIO":
        password = ""
    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_contraseña(password)
    
@when("hace click en el boton de login")    
def step_login_click(context):
    context.login_page.login_click()
    
@then("deberia ingresar al inventario")   
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url
    
@then('deberia mostrarse el mensaje de error "{mensaje}"')
def step_validar_mensaje_error(context,mensaje):
    error = context.login_page.get_error_message()
    assert mensaje in error,f"Se esperaba '{mensaje}',pero se obtuvo '{error}'"