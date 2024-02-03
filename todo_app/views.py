from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Todo, Contact


def home(request):
    return render(request,'home.html')



def todo(request):
    # if request.user.is_authenticated:
    #     user = request.user
    #     todos = Todo.objects.filter(user = user).order_by('priority')
    #     context = {
    #         'todos' : todos
    #     }
    #     return render(request, "todo.html" , context = context)
    # else:
    #     return render(request,'LogIn.html')
    
    return render(request, "todo.html")
    



def SignUp(request):
    # if request.method=="POST":
    #     get_name= request.POST.get('name')
    #     get_email= request.POST.get('email')
    #     get_password= request.POST.get('pass1')
    #     get_confirm_password= request.POST.get('pass2')
    #     if get_password == get_confirm_password:
    #         pass
    #     else:
    #         messages.info(request,'password is not matching')
    #         return redirect("/SignUp/")
        
    #     try:
    #         if User.objects.get(username=get_name):
    #             messages.warning(request,"This username is already in use!")
    #             return redirect("/SignUp/")
    #         if User.objects.get(email=get_email):
    #             messages.warning(request,"This email is already in use!")
    #             return redirect("/SignUp/")
    #     except Exception as identifier:
    #         pass

    #     myuser=User.objects.create_user(get_name,get_email,get_password)
    #     myuser.save()
    #     messages.success(request,"User is created please Log In!")        
    #     return redirect("/LogIn/")
    return render(request,'SignUp.html')




def handleLogin(request):
    # if request.method=="POST":
    #     get_name= request.POST.get('name')
    #     get_password= request.POST.get('pass1')
    #     myuser= authenticate(username=get_name,password=get_password)

    #     if myuser is not None:
    #         login(request,myuser) 
    #         messages.success(request,"Successfully LogIn")
    #         return redirect("/todo/")
    #     else:
    #         messages.error(request,"Invalid Credentials")
    #         return redirect("/LogIn/")
    return render(request,'LogIn.html')



 
def handleLogout(request):
    logout(request)
    messages.success(request,"LogOut Success")
    return render(request,'LogIn.html')




def AddTodo(request):
    # if request.user.is_authenticated:
    #     user = request.user
    #     print(user)

    #     if request.method=="POST":
    #         get_title= request.POST.get('title')
    #         get_status= request.POST.get('status')
    #         get_priority= request.POST.get('priority')
    #         duedate_start = request.POST.get('startdate')
    #         duedate_end = request.POST.get('enddate')

    #         mytodo = Todo(title=get_title, status=get_status, priority=get_priority, user=user , duedate_start = duedate_start, duedate_end = duedate_end)
    #         mytodo.save()
    #         print(mytodo)
    #     return redirect('/todo/')
    if request.method=="POST":
            get_title= request.POST.get('title')
            get_status= request.POST.get('status')
            get_priority= request.POST.get('priority')
            duedate_start = request.POST.get('startdate')
            duedate_end = request.POST.get('enddate')

            mytodo = Todo(title=get_title, status=get_status, priority=get_priority, duedate_start = duedate_start, duedate_end = duedate_end)
            mytodo.save()
            print(mytodo)
    return redirect('/todo/')
    


    
def Delete_Todo(request , id):
    Todo.objects.get(pk = id).delete()
    return redirect('todo')





def Edit_status(request , id , status):
    todo = Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('todo')





def contact(request):
    if request.method=="POST":
        get_first_name= request.POST.get('first_name')
        get_last_name= request.POST.get('last_name')
        get_email= request.POST.get('email')
        get_number= request.POST.get('number')
        get_msg= request.POST.get('msg')
        
        contact = Contact(first_name=get_first_name, last_name=get_last_name, email=get_email, number=get_number , msg = get_msg)
        contact.save()
        print(contact)
    return redirect('/')
