from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from datetime import date
from django.db.models import Sum
from .models import *
#from django.db import connection
from django.shortcuts import redirect 
from django.apps import apps
import psycopg2


def GET_fablab_worktypes(request):
    fablab_worktypes = WorkTypes.objects.order_by('-id')
    work_name = request.GET.get('work_name')

    if work_name:
        # Используйте функцию Q для объединения нескольких условий поиска
        filtered_data = fablab_worktypes.filter(
            Q(title__icontains=work_name) | Q(price__icontains=work_name)
        )
    else:
        filtered_data = fablab_worktypes.all()
        work_name = ""
    print(filtered_data)
    return render(request, "fablab_worktypes.html", {'filtered_data': filtered_data, 'search_value': work_name})

def view_fablab(request, process_id):
    worktype = WorkTypes.objects.get(id=process_id) # Берем один объект, находим его по id, которое получили в запросе
    return render(request, "view_fablab.html", {
        'work_list': worktype
    })
   
def delete_view_fablab(request, process_id):
    #worktype = Services.objects.get(id=process_id).delete() # Удаляем один объект, находим его по id, которое получили в запросе 
    conn = psycopg2.connect(dbname="fablabDB", host="localhost", user="postgres", password="123", port="5432")
    cursor = conn.cursor()
    cursor.execute("UPDATE \"worktypes\" SET for_counter=\'0\' WHERE id = %s", [process_id]) # посылаем туда SQL запрос
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("fablab_worktypes") # редиректимся на главную (метод fablab_worktypes)

def add_work(request, process_id):
    conn = psycopg2.connect(dbname="fablabDB", host="localhost", user="postgres", password="123", port="5432")
    cursor = conn.cursor()
    cursor.execute("UPDATE \"worktypes\" SET for_counter=\'1\' WHERE id = %s", [process_id]) # посылаем туда SQL запрос
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("fablab_worktypes") # редиректимся на главную (метод fablab_worktypes)

def count_works(request):
    fablab_worktypes = WorkTypes.objects.filter(for_counter=1)

    # Подсчет суммы количества
    summik = fablab_worktypes.count()   

    # Получение title услуг с for_counter = 1
    titles = fablab_worktypes.values_list('title', flat=True)
    print(titles)
    return render(request, "cart.html", {'summik': summik, 'titles': titles})
