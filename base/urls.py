from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup_form'),
    path('login/',views.login,name='login_form'),
    path('', views.home,name='home'),
    path('member/',views.member,name='member'),
    path('services/',views.services,name='services'),
    path('response/',views.reply,name='response')
]