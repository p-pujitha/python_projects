from django import forms
from django.core.urlresolvers import reverse
from .models import Post

from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout,
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ "username","title", "content" ,"image","user"]

    def get_success_url(self):
            return reverse("user_list")

User=get_user_model()

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*agrs, **kwargs):
        username= self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
       # user_qs=User.ojects.filter(username=uname)
        #if user_qs.count() == 1:
         #   user=user_qs.first()
        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("This user is not active")


        return super(UserLoginForm,self).clean(*agrs,**kwargs)



class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = [
            'username',
             'password'
        ]

