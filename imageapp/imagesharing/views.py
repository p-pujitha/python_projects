from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
)

from django.contrib.auth.models import User
from .forms import UserLoginForm,UserRegisterForm
from django.template.loader import get_template
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,User_details
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import classviews

# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        instance=form.save(commit = True)
        print form.cleaned_data.get("content")
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context ={
        "form":form,
    }
    return render(request, "post_form.html", context)


def post_detail(request,id=None): #retrieve
    #instance = Post.objects.filter(user_id__exact= id)
    instance = get_object_or_404(Post, id=id)
    context = {
        "instance" : instance,
        "title": instance.title
    }
    return render(request, "post_detail.html", context)
    #return HttpResponse("<h1>Detail </h1>")

def posts_ids(request,id=None): #retrieve
    instance = Post.objects.filter(user_id__exact= id)
    #instance = get_object_or_404(Post, user_id=id)
    context = {
        "object_list" : instance,
       # "title": instance.title
    }
    return render(request, "post_list.html", context)

def postsids(request,id=None): #retrieve
    instance = Post.objects.filter(user_id__exact= id)
    #instance = get_object_or_404(Post, user_id=id)
    context = {
        "object_list" : instance,
       # "title": instance.title
    }
    return render(request, "postlist.html", context)

def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)


    context = {
        "object_list": queryset,
        "title": "List"

    }

    """if request.user.is_authenticated():
        context={
            "title" : "My user List"
        }
    else:
        context = {
            "title" :"List"
        }
    """
    return render(request, "allposts.html", context)
    #return HttpResponse("<h1>List </h1>")




def post_update(request,id=None):
    instance = get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        messages.success(request,"Updated Successfully")
        return HttpResponseRedirect(instance.get_absolute_url())

    context= {
        "title" :instance.title,
        "instance":instance,
        "form":form
    }
    return render(request,"post_update.html",context)

def post_delete(request,id):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect("/profile/")

def user_list(request):
    all_users = User_details.objects.all()
    #template = get_template('user_det.html')
    context={
       'users':all_users
    }
    return render(request,"user_det.html",context)
    #result = template.render(context={'users': all_users}, request=request)
    #return HttpResponseRedirect(result)



def login_view(request):
    print (request.user.is_authenticated())
    title="Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request,user)
        print (request.user.is_authenticated())
        return redirect("/welcome/")

    return render(request,"loginform.html",{"form":form, "title":title})

def register_view(request):
    title="Register"
    form=UserRegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        newuser=authenticate(username=user.username,password=password)
        return redirect("/login/")
        #login_view(request)
    context={
        "form":form,
        "title":title
    }

    return render(request,"registerform.html",context)


def logout_view(request):
    logout(request)
    return render(request,"loginform.html",{})

def index(request):
    return render(request, 'start.html')

def welcome(request):

    return render(request,'welcome.html')


def profile(request):
    user_id = request.user.id
    instance = get_object_or_404(User_details, register_id=user_id)
    context = {
        "instance": instance,
        "user": instance.id
    }

    return render(request,'profile.html',context)