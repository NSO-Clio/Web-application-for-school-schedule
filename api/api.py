from flask import Flask, render_template, request, jsonify
from CreatTables import TableWorker


application = Flask(__name__, template_folder='templates')
tw = TableWorker(
    url='YOUR_URL',
    id_gid=[YOUR_ID],
    id_gid_consult=[YOUR_ID],
    path_service_account='TimeTable_serviceAcc.json'
)
tw.creatData()
tw.creatDataClasses()


@application.route('/application/TableWorker/v1')
def application_TableWorker_v1():
    return jsonify(tw.geter())


@application.route('/')
def homePage() -> str:
    return render_template('home.html')


@application.route('/time_table_choose_class')
def time_table_choose_class() -> str:
    return render_template('time_table.html', classes_data=tw.get_classes())


@application.route('/consalt_choose_teacher')
def consalt_choose_teacher() -> str:
    return render_template('consalt.html')


@application.route('/getTimeTable/<class_>')
def getTimeTableClass(class_: str) -> str:
    class_ = class_.lower().replace(' ', '')
    data = tw.get_Data(gid=True)[['Дни', 'Уроки', 'Время', class_]]
    data = [i for i in
            zip(
                data['Дни'].to_list(),
                data['Уроки'].to_list(),
                data['Время'].to_list(),
                data[class_].to_list()
            )
            ]
    return render_template(
        'time_table_for_class.html',
        dataLessons=data,
        class_=class_
    )


@application.route('/getTimeTableConsult/<teacher>')
def getTimeTableConsult(teacher: str) -> str:
    data = tw.get_Data(gid_consult=True)
    res_data = data[data['Учителя'] == teacher]
    dataConsultTeacher = [[i] + [' '.join(res_data[i].to_list()[0].split(' ')[:3])] +
                          [res_data[i].to_list()[0].split(' ')[-1]] for i in res_data.columns[1:]]
    return render_template(
        'consalt_TimeTable.html',
        teacher=teacher,
        dataConsultTeacher=dataConsultTeacher
    )


@application.route('/update_time_table')
def updateTimeTable():
    tw.creatData()
    return homePage()


@application.route('/AdminForm', methods=['POST'])
def adminForm():
    passwordAdmin = request.form['name']
    if passwordAdmin == 'YOUR_PASSWORD':
        return updateTimeTable()
    return homePage()


if __name__ == '__main__':
    application.run(debug=True)
