# Laboratorio Software Avanzado
## Práctica 8

En esta práctica de laboratorio se ha escrito un despliegue de una arquitectura que consta de un servidor de base de datos y un servidor web server escrito en python a través de contenedores y automatizando su despliegue a través de docker-composer. 


## Base de datos: Contenedor con Imagen Mysql:latest
Una base de datos Mysql con los siguientes datos. 
-   Password root
-   Nombre db: sa_db
-   Puerto: 3007 
-   Ejecuta el script setup.sql para iniciar la base de datos. 


Para ejecutar 

```bash
node app.js
```


## Servicio web 
Se ha desarrollado un servicio web que consume la base de datos y muestra el contenido en el 
navegador web. Escrito en Python3.7
Dependencias
-   Flask
-   Mysql connector


Para instalar las librerías necesarias:g
```bash
pip install -r requirements.txt
```

Para ejecutar 

```bash
flask run
```



## Despliegue de la arquitectura del sistema
Se requiere: 

-   Docker 19.03.13
-   Docker-compose 1.27.4

Para desplegar el sistema
```bash
docker-compose up
```





# Autor
  Erick Tejaxún
  erickteja@gmail.com
  201213050


## Licencia
[MIT](https://choosealicense.com/licenses/mit/)