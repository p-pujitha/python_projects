from django.shortcuts import render

# Create your views here.
from models import to_do_list, to_do_item
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader


def get_list(request):
    all_lists = to_do_list.objects.all()
    template = loader.get_template('lists.html')
    result = template.render(context={'lists': all_lists}, request=request)
    return HttpResponse(result)

def get_list_items(request, id):
    all_list_items = to_do_item.objects.filter(list_id__exact= id)
    template = loader.get_template('listitems.html')
    result = template.render(context={'items': all_list_items}, request=request)
    return HttpResponse(result)

def index(request):
    return render(request, 'todo_app/todostart.html')