from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('list', views.list_details, name='list_details'),
    path('add', views.add_detail, name='add_detail'),
]