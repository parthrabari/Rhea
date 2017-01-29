from django.conf.urls import url,include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/success',views.success,name= 'success'),
    url(r'^login/register',views.register,name= 'register'),


]
