Pasos para traer el repositorio a otro computador.

1. Crear carpeta en el directorio deseado
2. Dentro en la barra de direcciones damos click
3. Escribimos powershell y damos Enter
4. Validamos que en nuestro computador tengamos python instalado al igual que git
5. ejecutamos los siguientes comandos:
- git clone + el repositorio
- python -m venv myvenv (para recrear el myvenv) dentro del repositorio
- ir a activar (en myvenv/Scripts) => .\activate
- cd .. y cd ..
- python -m pip install --upgrade pip
- pip install -r requirements.txt (en el directorio raiz del repositorio)
- En la raiz, ejecutar python manage.py runserver

Nota1: En caso que arroje error de permisos de ejecucion de scripts, 
digitar el comando: Set-ExecutionPolicy Unrestricted
  
Debemos crear un superusuario para poder administrar las tablas a través del ambiente web de Django para visitar las tablas
python manage.py createsuperuser
