**Respuestas Conceptuales**

1. ¿Por qué hashear contraseñas?
Basicamente la razon fundamental es que almacenar contraseñas como texto plano seria una de las formas mas sencillas de facilitar ataques. Si un atacante logra acceder a la base de datos, obtendría directamente las claves reales de todos los usuarios. El hashing criptográfico resuelve esto porque no se puede revertirlo a su valor original pero trabaja de manera tal que el servidor recibe la clave que ingresa el usuario que pretende loguearse, le aplica el hasheo y compara con la que existe en la base de datos. 
A esto le agregue para el proyecto el uso de una libreria como Werkzeug que tiene una funcion que agrega una secuencia aleatoria unica a cada password antes de procesarlo, asegurando que en el caso de que 2 usuarios registraran identica contraseña, tengan cada una un hash diferente en la base de datos, lo cual brinda aun mayor seguridad. 

2. Ventajas de usar SQLite en este proyecto
No necesita instalar, levantar ni mantener un servidor de base de datos externo (como PostgreSQL, MariaDB o SQL Server). Se ejecuta directamente en el mismo proceso de la aplicación Python. Ademas esta integrado de forma nativa en python y es super liviano y por lo tanto 100% portable sin complicaciones
