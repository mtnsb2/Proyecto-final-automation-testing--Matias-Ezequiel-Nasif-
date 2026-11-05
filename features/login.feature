Feature: Inicio de sesion

    Scenario: Inicio de sesion exitoso
        Given que el usuario se encuentre en la pagina del login
        When ingresa en los campos de datos "usuario" y "contraseña"
        And hace click en el boton de login
        Then deberia ingresar al inventario
