from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Post
from .models import blog
from .models import enquery
from .forms import enqueryForm


def home(request):
    ob=Post.objects.all()
    ob1 = blog.objects.all()
    return render(request, 'index.html',{'obj':ob, 'ob':ob1})

def service(request):
    ob2 = blog.objects.all()
    return render(request, 'news.html',{'obj2':ob2})


def aboutus(request):
    return render(request, 'about.html')


def contact(request):
    # if(request.method=='POST'):
    #     n=request.POST['name']
    #     e=request.POST['email']
    #     s=request.POST['subject']
    #     m=request.POST['message']
    #     con=enquery.objects.create(name=n,email=e,subject=s,message=m)
    #     con.save()
    return render(request, 'contact.html')


def enquery(request):
    form = enqueryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = enqueryForm()
            return redirect('home:contact')
    return render(request, 'contact.html', {'form': form})

def logi(request):
    if(request.method=='POST'):
        u=request.POST['UserName']
        p=request.POST['Password']
        user=auth.authenticate(username=u, password=p)
        if user is not None:
            auth.login(request,user)
    return render(request, 'login.html')


def register(request):
    if (request.method == 'POST'):
        f = request.POST['firstname']
        u = request.POST['UserName']
        p = request.POST['password']
        e = request.POST['Email']
        l = request.POST['lastname']
        reg = User.objects.create_user(first_name=f, username=u, password=p, email=e, last_name=l,is_staff=True)
        reg.save()
        auth.login(request, reg)

    return render(request, 'register.html')
def detail(request):
    return render(request,'detail.html')
