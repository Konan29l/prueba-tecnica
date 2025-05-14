# Pruebas Tecnicas FastAPI Pruebas Unitarias.

Este proyecto implementa una API simple utilizando FastAPI para gestionar información de usuarios. Permite obtener detalles de un usuario por su ID y crear nuevos usuarios. También incluye pruebas unitarias para verificar la funcionalidad de la API.

El proyecto contiene dos archivos principales:

* "app.py": Define la aplicación FastAPI con dos rutas:
    * "/users/{user_id}" (GET): Obtiene la información de un usuario específico por su ID.
    * "/users/" (POST): Crea un nuevo usuario con un ID, nombre y edad.
* "test_app.py": Se presentan pruebas unitarias escritas con "pytest" para verificar el correcto funcionamiento de las rutas definidas en "app.py".

## Instalación

1.  Asegúrate de tener Python 3.8 o superior instalado en tu sistema.
2.  Clona este repositorio (si aún no lo has hecho).
3.  Navega al directorio del proyecto.
4.  Instala las dependencias necesarias:
    - pip install fastapi uvicorn pytest
  "fastapi" es el framework web, "uvicorn" es un servidor ASGI para ejecutar la aplicación, y "pytest" es el framework de pruebas.



## Cómo Levantar el Proyecto

Para ejecutar la API FastAPI, sigue estos pasos:

1.  Asegúrate de estar en el directorio del proyecto.
2.  Ejecuta el siguiente comando utilizando "uvicorn":
    
    uvicorn app:app --reload
   
    * "app": Se refiere al nombre del archivo Python ("app.py").
    * "app": Se refiere al nombre de la instancia de la aplicación FastAPI dentro del archivo "app.py" (en este caso, "app = FastAPI()").

3.  Una vez que el servidor se inicie, podrás acceder a la API en tu navegador. 

    * Para obtener un usuario (ejemplo para el usuario con ID "1"):
        
        GET [http://127.0.0.1:8000/users/1](http://127.0.0.1:8000/users/1)
        
    * Para crear un nuevo usuario (enviar una solicitud POST a `http://127.0.0.1:8000/users/?user_id=3&name=Olivia&age=40`). Puedes usar herramientas como "curl":
        
        curl -X POST "[http://127.0.0.1:8000/users/?user_id=3&name=Olivia&age=40](http://127.0.0.1:8000/users/?user_id=3&name=Olivia&age=40)"
        

## Cómo Ejecutar las Pruebas Unitarias

Para ejecutar las pruebas unitarias definidas en "test_app.py", sigue estos pasos:

1.  Asegúrate de estar en el directorio del proyecto.
2.  Ejecuta el siguiente comando utilizando "pytest":
    
    "pytest" buscará automáticamente los archivos que comiencen con "test_" y ejecutará las funciones de prueba dentro de ellos.

3.  Verás la salida de "pytest", indicando si las pruebas pasaron o fallaron. En este caso, se ejecutarán las pruebas para obtener usuarios existentes y no existentes, así como para crear usuarios exitosamente y al intentar crear un usuario que ya existe.
