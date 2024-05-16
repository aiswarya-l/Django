from .  import views
from django.contrib import admin
from django.urls import path, include

urlpatterns=[
    path('',views.index, name='index'),
    path('delete/<int:taskid>/', views.delete,name='delete'),
    path('update/<int:id>/', views.update,name='update')
    # path('details/',views.details,name='details'),
]