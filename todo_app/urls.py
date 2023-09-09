from django.contrib import admin
from django.urls import path, include
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home , name='home'),

    path('todo/', views.todo , name='todo'),
    
    path('contact/', views.contact , name='contact'),



    path('SignUp/', views.SignUp , name='SignUp'),

    path('LogIn/', views.handleLogin , name='handleLogin'),

    path('LogOut/', views.handleLogout , name='handleLogout'),

    path('AddTodo/', views.AddTodo , name='AddTodo'),

    path('Delete_Todo/<int:id>', views.Delete_Todo , name='Delete_Todo'),

    path('Edit_status/<int:id>/<str:status>', views.Edit_status , name='Edit_status'),



    

    


]