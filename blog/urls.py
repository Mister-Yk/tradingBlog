from django.urls import path
from .import views

urlpatterns = [
   path('', views.home, name="home"),
   path('blog', views.blog, name="blog"),
   path('detail', views.detail, name="detail"),
   path('projet', views.projetDetail, name="projetDetail"),
   path('contact', views.contact, name="contact"),


]