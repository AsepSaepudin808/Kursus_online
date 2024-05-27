from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Kursus,Siswa,Belajar
import datetime


# from django.http import HttpResponse

def index(request):
    data_kursus = Kursus.objects.all()
    return render(request,"index.html", {'judul':'Home', 'data': data_kursus})

def about(request):
    return render(request,"about.html", {'judul':'Tentang Saya'})

def register(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        no_handphone = request.POST.get('no_handphone')
        password = request.POST.get('password')
        if nama and email and no_handphone and password:
            user = User.objects.create_user(username=email,email=email,password=password)
            Siswa.objects.create(user_id = user.id, nama=nama, no_handphone=no_handphone)
            return render(request,"register_success.html")

    return render(request,"register.html", {'judul':'Registrasi'})

def login(request):
    if request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = auth.authenticate(username=email,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')


    return render(request,"login.html", {'judul':'Login'})

def logout(request):
    auth.logout(request)
    return redirect('home')

def kelasSaya(request):
    data = Belajar.objects.all().select_related('kursus').filter(user_id=request.user.id)
    return render(request,"kelas_saya.html", {'judul':'Kelas Saya','data':data})

def mendaftar(request,id):
    data = Kursus.objects.get(pk=id)
    if request.method=='POST':
        Belajar.objects.create(status=True,tanggal=datetime.date.today(),link='#',user_id=request.user.id,kursus_id=id)
        return redirect('kelas')
    return render(request,"mendaftar.html",{'data':data})