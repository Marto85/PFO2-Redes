**Respuestas Conceptuales**

1. ¿Por qué hashear contraseñas?
Porque guardar contraseñas en texto plano es muy riesgoso. Si alguien logra entrar a la base de datos, puede ver todas las claves reales de los usuarios y eso sería un problema serio. Por eso se usa el hashing, que transforma la contraseña en un valor cifrado que no se puede volver a la original. Cuando un usuario quiere iniciar sesión, la aplicación toma la contraseña que escribió, la hashea y la compara con la que está guardada. De esa forma, ni siquiera el sistema tiene que guardar la contraseña original.

En este proyecto usé Werkzeug, que ya trae funciones de hashing seguras. Además, agrega un valor aleatorio propio a cada contraseña antes de procesarla, así dos personas que tengan la misma contraseña no queden con el mismo hash en la base de datos. Esto hace que la seguridad sea mucho mejor.

2. Ventajas de usar SQLite en este proyecto
SQLite es una muy buena opción para este tipo de proyecto porque no necesita un servidor de base de datos separado. Se usa directamente dentro de la aplicación y es muy fácil de mantener. Además, viene integrado con Python, por lo que no hace falta instalar nada extra para usarlo. Es liviano, práctico y portátil, así que es ideal para proyectos pequeños o de aprendizaje como este.
