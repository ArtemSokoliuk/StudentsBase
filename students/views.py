# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse



# Views for Students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Соколюк',
         'last_name': u'Артем',
         'ticket': 2353,
         'image': 'img/1.jpg'},
        {'id': 2,
         'first_name': u'Орлов',
         'last_name': u'Валерій',
         'ticket': 2123,
         'image': 'img/2.jpg'},
        {'id': 3,
         'first_name': u'Степанов',
         'last_name': u'Андрей',
         'ticket': 4555,
         'image': 'img/3.jpg'},
    )
    return render(request, 'students/students_list.html',
                  {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'МГТ-101',
         'leader': {'id': 1, 'name': u'Соколюк Артем'}},
        {'id': 2,
         'name': u'МГТ-102',
         'leader': {'id': 2, 'name': u'Пинчук Олег'}},
        {'id': 3,
         'name': u'МГТ-103',
         'leader': {'id': 3, 'name': u'Степанов Ігор'}},
    )
    return render(request, 'students/groups_list.html',
                  {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


<<<<<<< HEAD
# Views for Journal
def journal(request):
    students = (
        {'id': 1,
         'first_name_surname': u'Соколюк Артем'},
        {'id': 2,
         'first_name_surname': u'Орлов Олег'},
        {'id': 3,
         'first_name_surname': u'Степанов Андрей'}

    )
    return render(request, 'students/journal.html',
                  {'journal': students})
=======
>>>>>>> dab3c75415194e02f7c8d1f5fdfb8ef94dea7bf1
