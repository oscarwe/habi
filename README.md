SERVICIO DE FILTRADO

Este proyecto se ha diseñado como un servicio web que proporciona filtrado de propiedades, con el objetivo de tener una arquitectura modular, escalable, seguro, reutilizable, legible y mantenible para posibles servicios futuros. 
Descripcion mas detallada del proyecto y los detalles detras de su dieño:
1. Clase BaseRESTHandler: Esta clase se ha creado como una clase base que maneja la lógica común necesaria para mas servicios web. Contiene métodos para la verificación del token JWT, la limpieza de cadenas, y la extracción de parámetros de las solicitudes HTTP, fue una clase pensada en la escalabilida y reutilizacion del codigo en caso de ser necesario pues sus funciones las pueden heredar otros posibles servicios promoviendo la modularidad y mantenibilidad del codigo.
2. Clase PropertyFilterService: Esta clase extiende BaseRESTHandler y proporciona la lógica específica para el servicio de filtrado de propiedades como la logica de negocio lo requeria. Utiliza la funcionalidad proporcionada por la clase base para la autenticación JWT y la extracción de parámetros de solicitud. La lógica de filtrado de propiedades se implementa en el método get_filtered_data donde se construye y ejecuta la consulta SQL utilizando los parámetros proporcionados parametrizados, esta parametrizacion fue pensada para simplificar el proceso de mantenimiento y desarrollo ya que no seria necesario desplegar codigo a produccion si se desea cambiar la consulta SQL y los parametros desde sus respectivas tablas.
3. Patron de diseño: La arquitectura del codigo sigue el principio de separacion de responsabilidades donde cada clase tiene una funcion clara y especifica con la posibilidad de ser reusada como es el caso de la clase BaseRESTHandler facilitando la comprension y mantenimiento.
4. Mitigacion de volnerabilidades: Se implementaron medidas de seguridad como la verificacion del token JWT para autenticar las solicitudes de los clientes, ademas de saneamientos a las cadenas de entrada para prevenir inyecciones de SQL y ataques a la base de datos.
5. Parametrizacion: Los datos sensibles fueron colocados en un archivo settings que idealmente sea un archivo no versionado si no que se manejaria como variables de entorno por ejemplo para tener esa capa extra de seguridad en informacion sensible a demas de poder configurar parametros unicamente moviendo variables sin necesidad de alterar codigo.
6. Documentacion incorporada: Se integraron comentarios y documentacion de las bibliotecas utilizadas facilitando su comprension y mantenimiento futuro
7. Manejo de excepciones: se implemento la gestion de errores para ser manejados adecuadamente sin entregarle informacion sensible al usuario pero dejandole claro las situaciones inesperadas

Archivos:
-filter_property_service.py: contiene la clase main donde se levanta el local server para hacer pruebas facilmente y logica de negocio para filtrar las propiedades
-base.py: contiene los handlers para peticiones RESTful, un codigo util y reutilizable
-secret_key.py: en este archivo se crean tokens JWT de manera manual para poder ser probados en un POSTMAN por ejemplo
-settings.py: este archivo vendria siendo como las variables de entorno que contiene informacion sensible y parametrizable
-test: contiene las pruebas unitarias
-requirements.txt: contiene las librerias necesarias para el correcto funcionamiento

Como correrlo:
Una vez descargado el repositorio, configura el entorno virtual en Python 3.9, instala las dependencias del archivo requirements.txt, ejecuta el script secret_key.py para obtener la llave JWT necesaria, copia la primera llave en el archivo settings.py en la variable SECRET_KEY y utiliza la segunda como token de autorización. Luego, ejecuta filter_property_service.py para iniciar el servidor. Finalmente, podrás acceder al servicio de filtrado de propiedades y realizar llamadas HTTP para obtener los resultados deseados.

SERVICIO DE LIKES

La tabla de likes se diseña de esta manera para garantizar que cada me gusta este asociado a un usuario registrado y a una propiedad. Al utilizar property_id y user_id como llaves foráneas establecemos una relación directa entre los likes, los usuarios y las propiedades, esto permite mantener un registro histórico de las interacciones de los usuarios con las propiedades, lo que facilita el análisis de datos y proporciona información valiosa para mejorar la experiencia del usuario y personalizar recomendaciones. Además al incluir el campo creation_date_time podemos registrar cuándo se realizó cada "me gusta" lo que añade contexto a los datos almacenados.

Script creacion:
CREATE TABLE Likes (
    like_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    user_id INT,
    creation_date_time DATETIME,
    FOREIGN KEY (property_id) REFERENCES Property(property_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

SEGUNDO EJERCICIO

En la carpeta segundo ejercicio se encuentra el script para este mismo, igual solamente se ejecuta como un script de python