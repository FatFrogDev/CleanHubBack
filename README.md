# CleanHub

Proyecto desarrollado para entrega final __PRIMER BLOQUE-TEORICO-PRACTICO - VIRTUAL/FRONT END__. Creado con Python, usando una base de datos postgresql [render](https://render.com/).

## Contenido

- [Tecnologías](#Tecnologías)
- [Dependencias](#Dependencias)
- [Como ejecutar](#Como-Ejecutar)


El proyecto está realizado con:

- python 3.11.9 | versión compatible
- Fastpi
- postgreSQL
- SqlAlchemy
- Uvicorn

## Dependencias

Las dependencias del proyecto se encuentran ubicadas en "requirements.txt". Cada dependencia contiene su respectiva versión.

## Configuración

Para la configuración del proyecto tenemos la configuración de la base de datos. En este caso se usa postgreSQL.
En el archivo `"db\db.py"` se encuentran los parámetros de configuración que debe ubicar en dicha variable. <br>
Los datos encerrados en `**` deben ser reemplazados siguiendo el ejemplo:

``` python
	DATABASE_URL="postgresql://*secretUser*:*scrtpwd1611*@*host*:*port*/*mydb*"
```

Para la configuración de CORS. Entre al archivo `"main.py"` y agregue los orígenes que necesite:


```  python
	origins=[
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:3000/",
	"http://another-host:8080/"
    ]
```

## Como Ejecutar

Clone el repositorio

``` sh
	git clone https://github.com/FatFrogDev/CleanHub
```
Entra al repositorio.
``` sh
	cd CleanHub
```

Para ejecutar el proyecto, se recomienda primero crear un entorno virtual ejecutando el siguiente comando en una consola CMD:

``` sh
	python -3.11 -m venv venv
```

Para activar el entorno virtual, ejecute el siguiente comando en la consola:

``` sh
	.\venv\Scripts\activate
```

> Nota: Se recomienda actualizar el instalador pip a la versión 24.2

Instale las dependencias del proyecto:

``` sh
	pip install -r requirements.txt
```

Por último, para correr el proyecto en sí, ejecute el siguiente comando:

```sh
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


Con este comando debe correr el proyecto correctamente. Tenga en cuenta que la bandera --reload hace que el servidor se mantenga en pie constantemente. Sin 
ella, ante un error considerable, el servidor se detiene.

## Despliegue

Para el despliegue del proyecto. Tras elegir el servicio con el que desplegará este backend. Debe configurar mediante el menú del proveedor, las variables de entorno, las cuales son:
>Nota: Las variables de entorno son accedidas mediante el método `"os.getenv()"`
```py
	FRONTEND_URL="https://frontend/"
```
Esta configuración añade a la configuración de CORS la variable de entorno proveída.<br>
La siguiente variable de entorno recae a la conexión con la base de datos.<br>
Debe ser configurada con el siguiente nombre. Cambie los valores según necesite.
```py
	DATABASE_URL="postgres/user:password@host:port/database"
```