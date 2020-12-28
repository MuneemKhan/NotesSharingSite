from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date

# Create your views here.

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def userlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email id']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login_admin.html', d)

def signup1(request):
    error=""
    if request.method=='POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        e = request.POST['emailid']
        p = request.POST['password']
        b = request.POST['department']
        r = request.POST['category']
        try:
            user = User.objects.create_user(username=e,password=p,first_name=f,last_name=l)
            Signup.objects.create(user=user,contact=c,department=b,category=r)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    return render(request,'admin_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data':data,'user':user}
    return render(request,'profile.html',d)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    error = False
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        b = request.POST['department']
        user.first_name = f
        user.last_name = l
        data.contact = c
        data.department = b
        user.save()
        data.save()
        error = True
    d = {'data':data,'user':user,'error':error}
    return render(request,'edit_profile.html',d)

def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c==n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'changepassword.html',d)

def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        b = request.POST['department']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),department=b,subject=s,notesfile=n,filetype=f,description=d,status='pending')
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'upload_notes.html',d)

def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.get(user=user)

    d = {'notes':notes}
    return render(request,'view_mynotes.html',d)