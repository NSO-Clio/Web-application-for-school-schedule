# Web-application-for-school-schedule

Веб приложение по расписанию для сенсорной электронной доски

# Заказчик

Данное приложение было разработанно по заказу МАОУ Лицей №22 "Надежда Сибири" в Новосибирской области, город Новосибирск 2023 год.

<img style="width: 70%; height: 70%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/logo22.jpg">

# Подключение аккаунта и всей таблицы

- Вам понадобиться ключ разработчика google для вашей таблици с расписанием

-	Ключ разработчика(json файл), который вы сохраните нужно переименовать как «TimeTable_serviceAcc»

-	После чего в коде файла api.py где указан url в кавычки вставить свой, а именно ссылка на вашу таблицу

-	После чего в переменных id_gid укать id таблиц, которые сделаны для расписания классов. Id страници указан в ссылке после слова «gid» в данном примере id 0
<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701598302.jpeg">

- В переменной id_gid_consult указать тоже id, но уже не на расписание классов, а на расписание консультаций

```python
tw = TableWorker(
    url='YOUR_URL',
    id_gid=[YOUR_ID],
    id_gid_consult=[YOUR_ID],
    path_service_account='TimeTable_serviceAcc.json'
)
```

# Запуск приложения

После того как вы сделаете все пункты выше вам придётся запустить файл api.py. Через консоль, открыв её внутри рабочей папки и прописать
```
python api.py
```

Потом в браузере перейти в по ссылке http://localhost:5000/ и включить полноэкранный режим.

Приложение запущено можно пользоваться

# Скринкаст приложения

<div style="margin: auto;">
<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600762.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600833.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600820.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600849.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600862.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600870.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600888.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600899.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600909.jpeg">

<img style="width: 40%; height: 40%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701600923.jpeg">
</div>

# Дополнительные заметки по администрированию

- Расписание для классов должно быть одного стиля для первой, второй смены и расписания консультаций
Пример:

Первая смена

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701598294.jpeg">

Вторая смена

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701598298.jpeg">

Консультации

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701598292.jpeg">

- Если в расписании произошло какое-либо обновление, вам нужно зайти во вкладку расписание или консультации и в самом низу подвале приложения находиться надпись. **Createb by SAMURAI_KOVSKI and EgorAndrik** Вам нужно будет на неё нажать, появиться форма для администратора где вы должны ввести пароль(если пароль не верный вас просто перенесёт на главную страницу)
Пароль: вы должны будете указать свой в функции
```python
def adminForm():
    passwordAdmin = request.form['name']
    if passwordAdmin == 'YOUR_PASSWORD':
        return updateTimeTable()
    return homePage()
```
Потом вам нужно подождать несколько секунд – минут и приложение обновит данные

- Если вы составили новую страницу, вам следует взять её id  добавить в соответствующую переменную после чего перезагрузить файл api.py, а именно прописать ``` python api.py ``` предварительно зайти в консоль на которой запущено api и нажать Ctrl + C чтобы завершить выполнение кода

# Наши контакты

**Андреасян Егор Андреасович**:
-	BackEnd and FullStack Dev
-	Почта: egorandreasyan@yandex.ru
-	Дополнительная почта: egorandreas28@gmail.com
-	Телегремм: https://t.me/EgorAndrik
-	Vk: https://vk.com/egor_andrik
-	Github: https://github.com/EgorAndrik 

**Пясковский Александр Михайлович**:
-	FrontEnd and FullStack Dev
-	Почта: alexanderpyaskovsky@yandex.ru 
-	Дополнительная почта: sashakedr@icloud.com 
-	Телегремм: https://t.me/SAMURAI_KOVSKI
-	Vk: https://vk.com/id457951126 
-	Github: https://github.com/SAMURAI2035 
