# Web-application-for-school-schedule

[![Code Size](https://img.shields.io/github/languages/code-size/NSO-OSKOM/Web-application-for-school-schedule)](https://github.com/NSO-OSKOM/Web-application-for-school-schedule)
<img alt="python" src="https://img.shields.io/badge/python-3.10.11-yellow.svg"/>

Scheduled web application for touchscreen electronic board.

# Customer

This application was developed by order of the MAOU Lyceum No. 22 "Nadezhda Siberia" in the Novosibirsk region, Novosibirsk 2023.

<img style="width: 70%; height: 70%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/logo22.jpg">

# Connecting the account and the entire table

- You will need a google developer key for your schedule table

- The developer key (json file) that you save needs to be renamed as “TimeTable_serviceAcc”

- Then, in the code of the api.py file where the url is specified, insert your own in quotes, namely a link to your table

- Then in the variables id_gid_one_sm and id_gid_two_sm specify the id of the tables that are made for the class schedule. The page id is indicated in the link after the word “gid” in this example id 0
<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701598302.jpeg">

- In the id_gid_consult variable, indicate the same id, but not for the class schedule, but for the consultation schedule
- The id_gid_sub_lesson variable is responsible for the schedule of extracurricular activities

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

# Launching the application

After you have completed all the steps above, you will have to download all the libraries that are used in the API and run the api.py file. Via the console, opening it inside the working folder and registering

- Downloading libraries
```
pip install -r requirements.txt
```

- Launching the API
```
python api.py
```

Then in your browser go to the link http://localhost:5000/ and enable full screen mode.

The application is running and you can use it

# Screencast of the application

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


# Additional Administration Notes

- The schedule for classes should be the same style for the first, second shift and consultation schedule

Example:

- First shift

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-25.jpg">

- Second shift

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-24.jpg">

- Consultations

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-21.jpg">

- Extracurricular activities are similar to the class schedule

 An example of a Google spreadsheet can be viewed here https://docs.google.com/spreadsheets/d/1ef__SA0CMETxDydDADxHaUU10-NLQmL6T16MOYVUznI/edit#gid=0 

- If there has been any update in the schedule, you need to go to the schedule or consultations tab and there will be an inscription at the very bottom of the application footer. **Createb by SAMURAI_KOVSKI and EgorAndrik** You will need to click on it, a form for the administrator will appear where you must enter a password (if the password is incorrect you will simply be transferred to the main page)
Password: you will have to specify yours in the function
```python
def adminForm():
    passwordAdmin = request.form['name']
    if passwordAdmin == 'YOUR_PASSWORD':
        return updateTimeTable()
    return homePage()
```
Then you need to wait a few seconds - minutes and the application will update the data

- If you have created a new page, you should take its id and add it to the appropriate variable, then reload the api.py file, namely, write ``` python api.py ``` first go to the console on which the api is running and press Ctrl + C to terminate code execution

# Our contacts

**Andreasyan Egor Andreasovich**:

> **BackEnd and FullStack Dev**

- E-mail: egorandreasyan@yandex.ru
- Additional e-mail: egorandreas28@gmail.com
- Telegram: https://t.me/EgorAndrik
- Vk: https://vk.com/egor_andrik
- Github: https://github.com/EgorAndrik 

**Pyaskovsky Alexander Mikhailovich**:

> **FrontEnd and FullStack Dev**

- E-mail: alexanderpyaskovsky@yandex.ru 
- Additional email: sashakedr@icloud.com 
- Telegram: https://t.me/SAMURAI_KOVSKI
- Vk: https://vk.com/id457951126 
- Github: https://github.com/SAMURAI2035 
