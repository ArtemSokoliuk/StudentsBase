# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


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

