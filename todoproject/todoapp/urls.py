from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:taskid>/',views.delete,name='delete')

]