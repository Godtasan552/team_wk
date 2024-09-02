from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# ฟังก์ชันที่ใช้สำหรับหน้าแรก
def indexPage(request):
    return render(request, 'index.html')

# ฟังก์ชันสำหรับการเข้าสู่ระบบ
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # หรือหน้าหลังจากเข้าสู่ระบบสำเร็จ
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ฟังก์ชันสำหรับการลงทะเบียน
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # หรือหน้าหลังจากลงทะเบียนสำเร็จ
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# ฟังก์ชันสำหรับหน้า home หลังจากเข้าสู่ระบบ
@login_required
def home_view(request):
    return render(request, 'home.html')
