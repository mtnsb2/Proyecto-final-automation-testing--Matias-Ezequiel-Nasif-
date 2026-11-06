#"x-api-key": "pub_726187485afa204b113fb01fe7deff0fb9aa6abc67c17700d9a86727c58ae792"  #agregar variable a api por seguridad
import pytest
import requests
import pytest_check as check
from utils.logger import logger


@pytest.mark.order(4)
def test_obtener_usuario(base_url,headers):
    logger.info("Inicio Pruebas de API")
    logger.info("Verificacion de Json")
    try:
        url = f"{base_url}/users/2" 
        
        response = requests.get(url,headers=headers)
        logger.info("Verificacion nivel 1")
        codigo = response.status_code
        assert codigo == 200
        data = response.json()
        print(data) #en caso de error muestra info correcta
        
        logger.info("Verificacion nivel 2")
        assert "application/json" in response.headers["Content-Type"]
        
        logger.info("Verificacion nivel 3")
        data =response.json()
        assert isinstance(data,dict)
        assert "data" in data
        assert isinstance(data["data"],dict)
        
        assert "id" in data ["data"]
        assert "email" in data ["data"]
        assert "first_name" in data ["data"]
        assert "last_name" in data ["data"]
        
        logger.info("Verificacion nivel 4")
        assert data ["data"] ["id"] == 2 
        assert data ["data"] ["email"] ==  "janet.weaver@reqres.in" 
        
        logger.info("Verificacion de tiempo")
        assert response.elapsed.total_seconds() < 4 
        logger.info("Prueba verificacion de Json exitosa")
        
    except Exception as e:
        logger.error(f"Error durante prueba de API: {e}", exc_info=True)
        raise
    
    
def test_crear_usuario(base_url,headers):
    logger.info("Prueba api POST")
    try:    
        logger.info("Aplicando comando POST")
        url = f"{base_url}/api/users/" 
        
        usuario = {
                "email":"kovu.guau@reqres.in",
                "first_name":"kovu",
                "last_name":"chispita"
            }
        
        response = requests.post(url,headers=headers,json=usuario)
        logger.info("Verificacion aplicacion de POST")
        
        logger.info("Verificacion nivel 1")
        assert response.status_code ==201
        
        logger.info("Verificacion nivel 2")
        assert "application/json" in response.headers["Content-Type"]
        
        logger.info("Verificacion nivel 3")
        data=response.json()
        check.is_in("email",data)
        check.is_in("first_name",data)
        check.is_in("last_name",data)
        check.is_in("id",data)
        
        #codigo global , anotado como comentario en caso de necesitar mas adelante
        ''' assert "email" in data
        assert "first_name" in data
        assert "last_name" in data
        assert "id" in data'''
        #
        
        logger.info("Verificacion nivel 4")
        check.equal(data["email"],usuario["email"])
        check.equal(data["first_name"],usuario["first_name"])
        check.equal(data["last_name"],usuario["last_name"])
        
        #codigo global , anotado como comentario en caso de necesitar mas adelante
        '''assert data ["email"] == usuario ["email"] 
        assert data ["first_name"] == usuario ["first_name"]
        assert data ["last_name"] == usuario ["last_name"]'''
        #
        
        logger.info("Verificacion de tiempo")
        assert response.elapsed.total_seconds() < 2
        
        logger.info("Prueba api POST exitosa ")
        
    except Exception as e:
            logger.error(f"Error durante prueba de API: {e}", exc_info=True)
            raise
            
        
        
    
def test_eliminar_usuario(base_url,headers):
    try:    
        logger.info("Prueba api DELETE")
        url = f"{base_url}/users/2"
        
        logger.info("Aplicando comando DELETE")
        response = requests.delete (url,headers=headers)
        
        logger.info("Verificacion aplicacion de DELETE")
        
        logger.info("Verificacion nivel 1")
        assert response.status_code == 204
        #assert "application/json" not in response.headers["Content-Type"] #delete check  #204 status code (redundancia en caso de necesitar verificar)
        
        logger.info("Verificacion nivel 2")
        assert "Content-Type" not in response.headers        
        
        logger.info("Verificacion nivel 3 Y 4")
        assert response.content == b""
        #assert len(response.content) == 0 #same test (redundancia)
        
        logger.info("Verificacion de tiempo")
        assert response.elapsed.total_seconds() < 2 
        
        logger.info("Prueba api DELETE exitosa ")
          
    
    except Exception as e:
                logger.error(f"Error durante prueba de API: {e}", exc_info=True)
                raise
    
    
    