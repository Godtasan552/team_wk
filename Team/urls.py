from django.urls import path
from .views import indexPage, login_view, signup_view, home_view

urlpatterns = [
    path('', indexPage, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),  # หน้า home หลังจากเข้าสู่ระบบ
]
