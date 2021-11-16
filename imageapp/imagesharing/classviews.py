from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from models import User_details,Post

class UserCreateView(CreateView):
    model = User_details
    fields = ['username', 'email', 'phonenumber','register']

    def get_success_url(self):
        return reverse("user_list")


class UserUpdateView(UpdateView):
    model=User_details
    fields=['username', 'email', 'phonenumber','register']

    def get_success_url(self):
        return reverse("user_list")

class UserDeleteView(DeleteView):
    model=User_details
    fields=['username','email','phonenumber','register']

    def get_success_url(self):
        return reverse("user_list")