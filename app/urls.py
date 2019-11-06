from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name="index"),
        path('about/',views.about,name="about"),
        path('services/',views.services,name="services"),
        path('causes/',views.causes,name="causes"),
        path('blog/',views.blog,name="blog"),
        path('contact/',views.contact,name="contact"),
        path('login-form/',views.loginform,name="login-form"),
        path('register-form/',views.registerform,name="register-form"),
        path('forgot-pswd-form/',views.forgotpswdform,name="forgot-pswd-form"),
        path('logoutform/',views.logoutform,name="logout"),


]