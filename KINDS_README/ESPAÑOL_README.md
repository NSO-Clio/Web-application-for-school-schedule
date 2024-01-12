# Web-application-for-school-schedule

[![Code Size](https://img.shields.io/github/languages/code-size/NSO-OSKOM/Web-application-for-school-schedule)](https://github.com/NSO-OSKOM/Web-application-for-school-schedule)
<img alt="python" src="https://img.shields.io/badge/python-3.10.11-yellow.svg"/>

Aplicación web programada para placa electrónica táctil

# Other languages

- [English](../KINDS_README/ENGLISH_README.md)
- [Español](../KINDS_README/ESPAÑOL_README.md)
- [Русский](../README.md)


# Cliente

Esta aplicación fue desarrollada por orden de la IEAM(Institución Educativa Autónoma Municipal) Lyceum №22 "Esperanza de Siberia" en la región de Novosibirsk, la ciudad de Novosibirsk 2023.

<img style="width: 70%; height: 70%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/logo22.jpg">

# Conectando la cuenta y toda la mesa

- Necesitará una clave de desarrollador de Google para su tabla de programación.

- La clave de desarrollador (archivo json) que guarda debe cambiarse de nombre a "TimeTable_serviceAcc"

- Luego, en el código del archivo api.py donde se especifica la URL, inserte la suya entre comillas, es decir, un enlace a su tabla.

- Luego en las variables id_gid_one_sm e id_gid_two_sm especificamos el id de las tablas que se realizan para el horario de clases. La identificación de la página se indica en el enlace después de la palabra "gid" en este ejemplo, identificación 0
<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701598302.jpeg">

- En la variable id_gid_consult indicar también el id, pero no para el horario de clases, sino para el horario de consultas
- La variable id_gid_sub_lesson es responsable del cronograma de actividades extraescolares

```python
tw = TableWorker(
    url='YOUR_URL',
    id_gid_one_sm=[YOUR_ID],
    id_gid_two_sm=[YOUR_ID],
    id_gid_consult=[YOUR_ID],
    id_gid_sub_lesson=[YOUR_ID],
    path_service_account='TimeTable_serviceAcc.json'
)
```

# Lanzando la aplicación

Una vez que haya completado todos los pasos anteriores, deberá descargar todas las bibliotecas que se utilizan en la API y ejecutar el archivo api.py. A través de la consola, abriéndola dentro de la carpeta de trabajo y registrándose

- Descargando bibliotecas
```
pip install -r requirements.txt
```

- Lanzando la API
```
python api.py
```

Luego, en su navegador, vaya al enlace http://localhost:5000/ y habilite el modo de pantalla completa.

La aplicación se está ejecutando y puedes usarla.

# Screencast de la aplicación

<div style="margin: auto;">
<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600762.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600833.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-53.jpg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-55.jpg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-49.jpg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-57.jpg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-39-03.jpg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-39-05.jpg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-39-07.jpg">
</div>


[!video](https://github.com/NSO-OSKOM/Web-application-for-school-schedule/assets/124351915/9652cb85-6f16-4de6-abb8-455c656fe08d)


# Notas de administración adicionales

- El horario de clases deberá ser el mismo estilo para el primer, segundo turno y horario de consultas.

Ejemplo:

- Primer turno

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-25.jpg">

- Segundo turno

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-24.jpg">

- Consultas

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-21.jpg">

- Las actividades extracurriculares son similares al horario de clases.

Se puede ver un ejemplo de una hoja de cálculo de Google en https://docs.google.com/spreadsheets/d/1ef__SA0CMETxDydDADxHaUU10-NLQmL6T16MOYVUznI/edit#gid=0

- Si ha habido alguna actualización en el cronograma, es necesario ir a la pestaña de cronograma o consultas y en la parte inferior del pie de página de la solicitud hay una inscripción. **Creado por SAMURAI_KOVSKI y EgorAndrik** Deberá hacer clic en él, aparecerá un formulario para el administrador donde deberá ingresar una contraseña (si la contraseña es incorrecta, simplemente será transferido a la página principal)
Contraseña: tendrás que especificar la tuya en la función
```python
def adminForm():
    passwordAdmin = request.form['name']
    if passwordAdmin == 'YOUR_PASSWORD':
        return updateTimeTable()
    return homePage()
```
Luego debes esperar unos segundos - minutos y la aplicación actualizará los datos.

- Si ha creado una nueva página, debe tomar su ID y agregarla a la variable apropiada y luego volver a cargar el archivo api.py, es decir, escribir ``` python api.py ``` primero vaya a la consola en la que está api se está ejecutando y presione Ctrl + C para terminar de ejecutar el código

# Nuestros Contactos

**Egor Andreasyan**:

> **BackEnd and FullStack Dev**

- E-mail: egorandreasyan@yandex.ru
- Additional e-mail: egorandreas28@gmail.com
- Telegram: https://t.me/EgorAndrik
- Vk: https://vk.com/egor_andrik
- Github: https://github.com/EgorAndrik 

**Alejandro Piaskovski**:

> **FrontEnd and FullStack Dev**

- E-mail: alexanderpyaskovsky@yandex.ru 
- Additional e-mail: sashakedr@icloud.com 
- Telegram: https://t.me/SAMURAI_KOVSKI
- Vk: https://vk.com/id457951126 
- Github: https://github.com/SAMURAI2035 
