from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from models import to_do_list,to_do_item


class ListCreateView(CreateView):
    model = to_do_list
    fields = ['name', 'create_date']

    def get_success_url(self):
        return reverse("list_details")

class ListUpdateView(UpdateView):
    model=to_do_list
    fields=['name','create_date']

    def get_success_url(self):
        return reverse("list_details")

class ListDeleteView(DeleteView):
    model=to_do_list
    fields=['name','create_date']

    def get_success_url(self):
        return reverse("list_details")

class ItemUpdateView(UpdateView):
    model=to_do_item
    fields=['description','due_date','completed','list']

    def get_success_url(self):
        return reverse("list_details")

class ItemDeleteView(DeleteView):
    model=to_do_item
    fields=['description','due_date','completed','list']

    def get_success_url(self):
        return reverse("list_details")



class ItemCreateView(CreateView):
    model=to_do_item
    fields=['description','due_date','completed','list']

    def get_success_url(self):
        return reverse("list_details")



