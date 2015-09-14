# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse



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


