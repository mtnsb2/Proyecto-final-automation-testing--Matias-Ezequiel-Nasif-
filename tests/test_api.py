#"x-api-key": "pub_726187485afa204b113fb01fe7deff0fb9aa6abc67c17700d9a86727c58ae792"  #agregar variable a api por seguridad

import requests
import pytest_check as check

def test_obtener_usuario(base_url,headers):
    url = f"{base_url}/users/2" #placeholder
     
    response = requests.get(url,headers=headers)
    
    codigo = response.status_code
    print(codigo) # quizas borrar despuesA
    assert codigo == 200
    data = response.json()
    print(data) # quizas borrar despues
    assert "application/json" in response.headers["Content-Type"]
    
    data =response.json()
    assert isinstance(data,dict)
    assert "data" in data
    assert isinstance(data["data"],dict)
    
    assert "id" in data ["data"]
    assert "email" in data ["data"]
    assert "first_name" in data ["data"]
    assert "last_name" in data ["data"]
    
    assert data ["data"] ["id"] == 2 #placeholder value
    assert data ["data"] ["email"] ==  "janet.weaver@reqres.in" #placeholder email
    
    assert response.elapsed.total_seconds() < 2 #placeholder time
    
    
def test_crear_usuario(base_url,headers):
    url = f"{base_url}/api/users/" #placeholder
    
    
    usuario = {
            "email":"wwwwww",#placeholder
            "first_name":"wwww",#placeholder
            "last_name":"wwwww"#placeholder
        }
    
    response = requests.post(url,headers=headers,json=usuario)
    
    assert response.status_code ==201
    
    assert "application/json" in response.headers["Content-Type"]
    
    data=response.json()
    check.is_in("email",data)
    check.is_in("first_name",data)
    check.is_in("last_name",data)
    check.is_in("id",data)
    
    ''' assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "id" in data'''
    
    check.equal(data["email"],usuario["email"])
    check.equal(data["first_name"],usuario["first_name"])
    check.equal(data["last_name"],usuario["last_name"])
    
    '''assert data ["email"] == usuario ["email"]
    assert data ["first_name"] == usuario ["first_name"]
    assert data ["last_name"] == usuario ["last_name"]'''
    
    
    assert response.elapsed.total_seconds() < 2 #placeholder time
    
    
    #assert "application/json" not in response.headers["Content-Type"] #delete check  #204 status code
    
def test_eliminar_usuario(base_url,headers):
    url = f"{base_url}/users/2"
    
    response = requests.delete (url,headers=headers)
    
    assert response.status_code == 204
    
    assert "Content-Type" not in response.headers        
    
    assert response.content == b""
    #assert len(response.content) == 0 #same test
    
    assert response.elapsed.total_seconds() < 2 

    
    
    