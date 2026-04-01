from django.shortcuts import render
from .models import Education

def boulangerie(request):
    pictures = {
        'photo_1' : '1.jpg',
        'photo_2' : '2.jpg',
        'photo_3' : '3.jpg',
        'photo_4' : '10.jpg',
        'photo_5' : '4.jpg',
        'photo_6' : '9.jpg',
    }

    return render(request, 'boulangerie.html', {
        'pictures': pictures})

def education(request):
    about = {
        'full_name': 'Рябцева Мария Дмитриевна',
        'photo': '19.jpg',
        'email': 'mdryabtseva@edu.hse.ru',
        'phone': '+9 999 999-99-99'
    }
    
    program = {
        'name': 'Экономика',
        'description': 'Программа «Экономика» НИУ ВШЭ позволяет получить диплом бакалавра в ведущем российском вузе, выпускников которого охотно принимают на работу крупнейшие российские и международные компании, в государственные организации, в исследовательские центры и ведущие университеты. Программа включает в себя глубокое освоение экономической теории, методов математического анализа, статистики, эконометрики, способов обработки информации, программирования и изучение иностранных языков,  а также курсы прикладных финансовых и экономических дисциплин и научно-проектную работу.',
    }
    
    study_office = {
        'academic_name': 'Букин Кирилл Александрович',
        'academic_photo': '15.jpg',
        'academic_email': 'kbukin@hse.ru',
        'manager_name': 'Макарова Галина Викторовна',
        'manager_photo': '16.jpg',
        'manager_email': 'gmakarova@hse.ru'
    }
    
    classmates = [
        {
            'name': 'Албанова Анастасия',
            'photo': '17.jpg',
            'email': 'alb@edu.hse.ru',
            'phone': '+8 888 888-88-88'
        },
        {
            'name': 'Милько Анна',
            'photo': '18.jpg',
            'email': 'mil@edu.hse.ru',
            'phone': '+7 777 777-77-77'
        }
    ]
    
    return render(request, 'education.html', {
        'about': about,
        'program': program,
        'study_office': study_office,
        'classmates': classmates
    })

def menu(request):
    return render(request, 'menu.html')

def task(request):
    result = None
    if request.method == 'POST':
        data = request.POST.get('data', '')
        threshold_str = request.POST.get('threshold', '')
        try:
            threshold = float(threshold_str)
            subjects = {}
            parts = data.split('; ')
            for i in parts:
                name, grades_str = i.split(': ')
                grades = list(map(int, grades_str.split('-')))
                avg = sum(grades) / len(grades)
                subjects[name] = avg
            ok = [name for name, avg in subjects.items() if avg > threshold]
            ok.sort()
            result = ', '.join(ok) if ok else ''
        except Exception as e:
            result = "Ошибка ввода. Проверьте формат данных."
    return render(request, 'task.html', {'result': result})