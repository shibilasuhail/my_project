from django.urls import path
from .import views
app_name='home'
urlpatterns=[
    path('', views.home,name="home"),
    path('service/',views.service,name="service"),
    path(' aboutus/',views.aboutus,name="aboutus"),
    path('contact/' ,views.enquery,name="contact" ),
    path('Login/',views.logi,name="login"),
    path('register/',views.register,name="register" ),
    path('detail/',views.detail,name="detail"),
]