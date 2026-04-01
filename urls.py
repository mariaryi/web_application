from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pyscripts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('education/', views.education, name='edu'),
    path('boulangerie/', views.boulangerie, name='boulangerie'),
    path('menu/', views.menu, name='menu'),
    path('task/', views.task, name='task')
]