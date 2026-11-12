# TESTS PROYECTO FINAL
                                                       
Proyecto final QA Automation cursada 26221 saucedemo.com                                
## Objetivos del proyecto
- Mostrar conocimientos adquiridos en clases virtuales
- Realizar pruebas en distintas secciones de la URL indicada (www.saucedemo.com)
- Utilizacion del software detallado en README
- Entrega del proyecto final utilizando lo ya aplicado en la preentrega y conocimientos adquiridos posteriormente
## Tecnologia/software y utilizado                   
- Visual Code Studio                               
- Python              
- Github
- git
- pytest                        
- Selenium
- CSV
- Json
- Requests
- Behave
## Links de software utilizado
- https://code.visualstudio.com/
- https://www.python.org/
- https://github.com/
- https://reqres.in/
## Comandos para instalar software en Visual Code Studio
``` 
- pip install -U pytest
- pip install selenium
- pip install requests
- pip install behave
```
## Comandos utilizados para git
```
-  git config --global user.name " "  #NOMBRE DE USUARIO
-  git config --global user.emal " "  #EMAIL UTILIZADO
-  git init
-  git add .
-  git add README.md
-  git commit -m " "  #NOMBRE DEL COMMIT
-  git branch -M main
-  git remote add origin " " #DIRECCION DEL REPOSITORIO
-  git push -u origin main
```
## Comandos utilizados para realizar pruebas con pytest
```
- python -m pytest tests/ -s -v --html=reports/reporte.html 
- python -m pytest tests_sim_error/ -s -v --html=reports/reporte.html #test de simulacro de error #

```
## Extra
- Carpeta tests_sim_error contiene pruebas con errores para mostrar el funcionamiento correcto del reporte html y captura de screenshots ,las pruebas de error estan deshabilitadas via CI/CD pero general el reporte correcto si se habilitan (borrando o comentando el codigo "--ignore=tests_sim_error" en tests.yml)